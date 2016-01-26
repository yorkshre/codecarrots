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


class Patronage(models.Model):
    PATRON = 0
    PARTNER = 1
    SPONSOR = 2
    STATUS_CHOICES = (
        (PATRON, 'Patron'),
        (PARTNER, 'Partner'),
        (SPONSOR, 'Sponsor'),
    )
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='partners/')
    type = models.SmallIntegerField(choices=STATUS_CHOICES)

    @staticmethod
    def list():
        patrons = Patronage.objects.all().filter(type=Patronage.PATRON)
        partners = Patronage.objects.all().filter(type=Patronage.PARTNER)
        sponsors = Patronage.objects.all().filter(type=Patronage.SPONSOR)
        return {
            'patrons': patrons,
            'partners': partners,
            'sponsors': sponsors,
            'size_patrons': 0 if len(patrons) == 0 else int(12 / len(patrons)),
            'size_partners': 0 if len(partners) == 0 else int(12 / len(partners)),
            'size_sponsors': 0 if len(sponsors) == 0 else int(12 / len(sponsors)),
        }


class Menu:
    @staticmethod
    def options():
        return [
            {'title': 'Aktualności', 'href': '/'},
            {'title': 'O nas', 'href': '/onas'},
            {'title': 'Kontakt', 'href': '/kontakt'},
        ]


class Bio(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField()
    img = models.ImageField(upload_to='bios/')

    def publish(self):
        self.save()

    def __str__(self):
        return self.name
