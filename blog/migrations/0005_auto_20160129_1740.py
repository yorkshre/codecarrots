# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import blog.dropboxstorage
import blog.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20160126_2312'),
    ]

    operations = [
        migrations.AddField(
            model_name='patronage',
            name='url',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='bio',
            name='img',
            field=blog.models.DropboxImageField(upload_to='', storage=blog.dropboxstorage.DropBoxStorage()),
        ),
        migrations.AlterField(
            model_name='patronage',
            name='img',
            field=blog.models.DropboxImageField(upload_to='', storage=blog.dropboxstorage.DropBoxStorage()),
        ),
    ]
