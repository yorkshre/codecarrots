# Dokumentacja aplikacji przygotowanej na potrzeby konferencji codecarrots w Koszalinie


## Konfiguracja deweloperska:
### Szykujemy virtualenva w wersji pythona 3.4
```bash
virtualenv -p /usr/bin/python3.4 venv
```
### Musimy posiadać konto w serwisie dropbox. Tworzymy nową aplikację https://www.dropbox.com/developers/apps/create, najlepiej z dedykowanym folderem. Klikamy "Generate acccess token". Przyjmując, że nasz wirtualenv jest w folderze .venv konfigurujemy skyrpt .venv/bin/activate,
dodajemy wpis:
```bash
echo '
export DROPBOX_OAUTH2_TOKEN="**TU TWOJ TOKEN APLIKACJI DROPBOX**"
export NOREPLY_ACCOUNT="twoj_adres@email.com"
export NOREPLY_PASSWORD="magiczneHaslo"
export NOREPLY_TARGET=""
export RECAPTCHA_SITE_KEY=""
export RECAPTCHA_SECRET_KEY=""
' >> ~/.bashrc
```
### Tworzymy pustą bazę sqllite i migrujemy modele.
```bash
python manage.py migrate
```
### Na wszelki wypadek zbieramy wszystkie elementy statyczne
```bash
python manage.py collectstatic
```
### Uruchamiamy aplikację.
```bash
python manage.py runserver 127.0.0.1:3000
```
## Konfiguracja z heroku
### W folderze projektu wywołujemy
```bash
heroku create
```
Wynikiem działnia będzie dodanie listy repozytoriów repozytorium heroku.
### Ustawiamy niezbędne zmienne
```bash
heroku config:set DJANGO_STATIC_HOST="http://codecarrots-koszalin.herokuapp.com/"
heroku config:set DROPBOX_OAUTH2_TOKEN="**TU TWOJ TOKEN APLIKACJI DROPBOX**"
heroku config:set NOREPLY_ACCOUNT="twoj_adres@email.com"
heroku config:set NOREPLY_PASSWORD="magiczneHaslo"
heroku config:set NOREPLY_TARGET=""
heroku config:set RECAPTCHA_SITE_KEY=""
heroku config:set RECAPTCHA_SECRET_KEY=""
heroku config:set DEBUG=0
```
### Wypychamy naszą aplikację na serwer heroku
```bash
git push heroku master
```
### Upewniamy się, że wypchnięta przez nas instancja działa
```bash
heroku ps:scale web=1
```
### Uruchamiamy migracje
```bash
heroku run python manage.py migrate
```
### A następnie kolekcjonujemy wszystkie elementy statyczne w jedno
```bash
heroku run python manage.py collectstatic
```
### Otwieramy strone apki
```bash
heroku open
```
### W przypadku błędów sprawdzamy logi.
```bash
heroku logs --tail
```

## Materiały z kursu
W celu zdobycia pracy z materiałami kursu należy sklonować oficjalne repozytorium
```bash
git clone https://github.com/Draqun/django-carrots.git
```
