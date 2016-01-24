from django.db import models

from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Patronage():
    @staticmethod
    def list():
        patrons = [
        { "src":"/static/img/fundacja_infolet.jpg"},
        { "src":"/static/img/osworld.jpg"},
        ]
        partners = [
        { "src":"/static/img/infolet.jpg"},
        { "src":"/static/img/osworld.jpg"},
        ]
        sponsors = [
        { "src":"/static/img/indeks.jpeg"},
        ]
        return {
        'patrons':patrons,
        'partners':partners,
        'sponsors':sponsors,
        'size_patrons' : int(12/len(patrons)),
        'size_partners': int(12/len(partners)),
        'size_sponsors' : int(12/len(sponsors)),
    }


class Menu():
    @staticmethod
    def options():
        return [
            {'title':'Aktualności', 'href':'/'},
            {'title':'O nas', 'href':'/onas'},
            {'title':'Kontakt', 'href':'/kontakt'},
        ]
