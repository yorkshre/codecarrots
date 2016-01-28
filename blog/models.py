from django.db import models
from django.utils import timezone
from blog.dropboxstorage import DropBoxStorage

dstorage = DropBoxStorage()

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

class DropboxImageField(models.ImageField):
    def pre_save(self, model_instance, add):
        file = super(models.ImageField, self).pre_save(model_instance,add)
        file.name = self.storage.generate_url(file.name)
        return file

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
    img = DropboxImageField(storage=dstorage)
    type = models.SmallIntegerField(choices=STATUS_CHOICES)

    @staticmethod
    def list():
        patrons = Patronage.objects.all().filter(type=Patronage.PATRON)
        partners = Patronage.objects.all().filter(type=Patronage.PARTNER)
        sponsors = Patronage.objects.all().filter(type=Patronage.SPONSOR)
        return [
            {
                'label': "Partnerzy",
                'list': partners,
                'size': 6 if len(partners) <= 1 else 4 if len(partners) > 3 else int(12 / len(partners)),
                'single': len(partners) == 1
            },
            {
                'label': "Sponsorzy",
                'list': sponsors,
                'size': 6 if len(sponsors) <= 1 else 4 if len(sponsors) > 3 else int(12 / len(sponsors)),
                'single': len(sponsors) == 1
            },
            {
                'label': "Patroni",
                'list': patrons,
                'size': 6 if len(patrons) <= 1 else 4 if len(patrons) > 3 else int(12 / len(patrons)),
                'single': len(patrons) == 1
            },
        ]


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
    img = DropboxImageField(storage=dstorage)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name
