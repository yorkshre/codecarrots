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
        if "dropboxusercontent" in file.name:
            return file
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
    url = models.CharField(max_length=200, default="", blank=True)

    def __str__(self):
        return self.name

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
            {'title': 'Materiały', 'href': '/', 'list':
                [
                {'title': 'Warsztaty', 'href': '/static/doc/index.html'},
                {'title': 'Python', 'href': 'https://docs.python.org/3/'},
                {'title': 'Pliki', 'href': '/pliki'}
                ]
            },
            {'title': 'Kontakt', 'href': '/kontakt'},
        ]

class Links:
    @staticmethod
    def all():
        return [
            {'name': 'jap_dict.txt', 'url': 'https://dl.dropboxusercontent.com/s/mlv6i2tqk7dckdr/jap_dict.txt?dl=1'},
            {'name': 'encoded_msg.txt', 'url': 'https://dl.dropboxusercontent.com/s/34nctd0z6je733f/encoded_msg.txt?dl=1'},
            {'name': 'hangman.py', 'url': 'https://dl.dropboxusercontent.com/s/a4u6m39krie4cc5/hangman.py?dl=1'},
            {'name': 'message.py', 'url': 'https://dl.dropboxusercontent.com/s/y7gfweav7vchnn5/message.py?dl=1'},
            {'name': 'japanise_agata.py', 'url': 'https://dl.dropboxusercontent.com/s/xsoiq7l3tdqoxwb/japanise_agata.py?dl=1'},
            {'name': 'palindrom_agata.py', 'url': 'https://dl.dropboxusercontent.com/s/hxcqn2tempnkems/palindrom_agata.py?dl=1'},
            {'name': 'number_game_agata.py', 'url': 'https://dl.dropboxusercontent.com/s/ebncuafrtb3i9wh/number_game_agata.py?dl=1'},
            {'name': 'damian_hangman_game.py', 'url': 'https://www.dropbox.com/s/kcnajih2n5s0fjd/hangman_game.py?dl=1'},
            {'name': 'damian_japanise.py', 'url': 'https://www.dropbox.com/s/jmmgrgwm1vgn4uz/japanise.py?dl=1'},
            {'name': 'damian_message.py', 'url': 'https://www.dropbox.com/s/omkhx2gykfstcp8/message.py?dl=1'},
            {'name': 'damian_numbers.py', 'url': 'https://www.dropbox.com/s/1xw676uoyvos3ql/numbers.py?dl=1'},
            {'name': 'damian_palindrom.py', 'url': 'https://www.dropbox.com/s/1hfxingobntfrb2/palindrom.py?dl=1'},
            {'name': 'Wideokurs Django Wstęp', 'url': 'https://www.dropbox.com/s/f84dluvwmv8b4xs/00%20-%20Wst%C4%99p.ogv?dl=1'},
            {'name': 'Wideokurs Django Instalacja', 'url': 'https://www.dropbox.com/s/6cr4cow2r4sf2gx/01%20-%20Instalacja%20Pythona%20i%20Django.ogv?dl=1'},
            {'name': 'Wideokurs Django IDE', 'url': 'https://www.dropbox.com/s/h25rf51h8iw5og1/02%20-%20IDE%20i%20wtyczka%20do%20Pythona.ogv?dl=1'},
            {'name': 'Wideokurs Django Hello world', 'url': 'https://www.dropbox.com/s/szr2nw674tltdb6/03%20-%20Hello%20World%20w%20Django.ogv?dl=1'},
            {'name': 'Wideokurs Django Modele i migracje', 'url': 'https://www.dropbox.com/s/mff50mza7xencld/04%20-%20Modele%20i%20migracje.ogv?dl=1'},
            {'name': 'Wideokurs Django Formularze cz. 1', 'url': 'https://www.dropbox.com/s/8gjkd8uoy7dy5r3/05%20-%20Formularze%20cz.%201.ogv?dl=1'},
            {'name': 'Wideokurs Django Formularze cz. 2', 'url': 'https://www.dropbox.com/s/l909ynqzvc8l3vt/06%20-%20Formularze%20cz.%202.ogv?dl=1'}
        ]


class Bio(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField()
    img = DropboxImageField(storage=dstorage)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name
