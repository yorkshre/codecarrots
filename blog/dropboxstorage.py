# Dropbox storage class for Django pluggable storage system.
# Author: Anthony Monthe <anthony.monthe@gmail.com>
# License: BSD
#
# Usage:
#
# Add below to settings.py:
# DROPBOX_OAUTH2_TOKEN = 'YourOauthToken'

from __future__ import absolute_import
from django.utils.deconstruct import deconstructible
from datetime import datetime
import re
from urllib import request

from django.core.files.base import File
from django.core.exceptions import ImproperlyConfigured
import json
#from . import BytesIO, Storage
from storages.utils import setting

from dropbox.client import DropboxClient
import django
try:
    from django.utils.deconstruct import deconstructible
except ImportError:  # Django 1.7+ migrations
    deconstructible = lambda klass, *args, **kwargs: klass

# Storage only accepts `max_length` in 1.8+
if django.VERSION >= (1, 8):
   from django.core.files.storage import Storage, FileSystemStorage
else:
    from django.core.files.storage import Storage as DjangoStorage
    from django.core.files.storage import FileSystemStorage as DjangoFileSystemStorage

    class StorageMixin(object):
        def save(self, name, content, max_length=None):
            return super(StorageMixin, self).save(name, content)

        def get_available_name(self, name, max_length=None):
            return super(StorageMixin, self).get_available_name(name)

    class Storage(StorageMixin, DjangoStorage):
        pass

    class FileSystemStorage(StorageMixin, DjangoFileSystemStorage):
        pass

DATE_FORMAT = '%a, %d %b %Y %X +0000'


class DropBoxStorageException(Exception):
    pass


class DropBoxFile(File):
    def __init__(self, name, storage, mode='rb'):
        self.name = name
        self._storage = storage

    def read(self, num_bytes=None):
        return self._storage._read(self.name, num_bytes=num_bytes)

    def write(self, content):
        self._storage._save(self.name, content)




@deconstructible
class DropBoxStorage(Storage):
    """DropBox Storage class for Django pluggable storage system."""
    def generate_url(self, name):
        url = self.client.share(name, name)
        url = url['url']
        f = request.urlopen(url)
        path = f.geturl()
        return re.sub('www.dropbox.com','dl.dropboxusercontent.com', path)

    def url(self, name):
        return name #

    def __init__(self, oauth2_access_token=setting('DROPBOX_OAUTH2_TOKEN')):
        if oauth2_access_token is None:
            raise ImproperlyConfigured("You must configure a token auth at"
                                       "'settings.DROPBOX_OAUTH2_TOKEN'.")
        self.client = DropboxClient(oauth2_access_token)

    def delete(self, name):
        self.client.file_delete(name)

    def exists(self, name):
        response = self.client.search('/', name, file_limit=1)
        return bool(response)

    def listdir(self, path):
        directories, files = [], []
        metadata = self.client.metadata(path)
        for entry in metadata['contents']:
            if entry['is_dir']:
                directories.append(entry['path'])
            else:
                files.append(entry['path'])
        return directories, files

    def size(self, name):
        metadata = self.client.metadata(name)
        return metadata['bytes']

    def modified_time(self, name):
        metadata = self.client.metadata(name)
        mod_time = datetime.strptime(metadata['modified'], DATE_FORMAT)
        return mod_time

    def accessed_time(self, name):
        metadata = self.client.metadata(name)
        acc_time = datetime.strptime(metadata['client_mtime'], DATE_FORMAT)
        return acc_time

    def _open(self, name, mode='rb'):
        remote_file = DropBoxFile(name, self)
        return remote_file

    def _save(self, name, content):
        self.client.put_file(name, content)
        return name

    def _read(self, name, num_bytes=None):
        data = self.client.get_file(name)
        return data.read(num_bytes)