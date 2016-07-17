# Dokumentacja aplikacji przygotowanej na potrzeby konferencji codecarrots w Koszalinie
###
#### Konfiguracja deweloperska:
1. Szykujemy virtualenva w wersji pythona 3.4
```bash
virtualenv -p /usr/bin/python3.4 venv
```
2. Musimy posiadać konto w serwisie dropbox. Tworzymy nową aplikację https://www.dropbox.com/developers/apps/create, najlepiej z dedykowanym folderem. Klikamy "Generate acccess token". Przyjmując, że nasz wirtualenv jest w folderze .venv konfigurujemy skyrpt .venv/bin/activate,
dodajemy wpis:
```bash
DROPBOX_OAUTH2_TOKEN="**TU TWOJ TOKEN APLIKACJI DROPBOX**"
echo '
export DROPBOX_OAUTH2_TOKEN="**TU TWOJ TOKEN APLIKACJI DROPBOX**"
export NOREPLY_ACCOUNT="twoj_adres@email.com"
export NOREPLY_PASSWORD="magiczneHaslo"
export NOREPLY_TARGET=""
export RECAPTCHA_SITE_KEY=""
export RECAPTCHA_SECRET_KEY=""
' > ~/.bashrc
```
3. Tworzymy pustą bazę sqllite i migrujemy modele.
```bash
python manage.py migrate
```
4. Uruchamiamy aplikację.
```bash
python manage.py runserver 127.0.0.1:3000
```
##### Uwagi:
###### Pliki wrzucane do bazy w administracji aplikacji wrzucane sa produkcyjne na moje (lukasz zielinski) konto dropboksa. Klucz znajduje sie w konfiguracji aplikacji na heroku


#### Konfiguracja z heroku
1. W folderze projektu wywołujemy
```bash
heroku create
```
Wynikiem działnia będzie dodanie listy repozytoriów repozytorium heroku.
2. Ustawiamy niezbędne zmienne
```bash
heroku config:set DISABLE_COLLECTSTATIC=1
heroku config:set DROPBOX_OAUTH2_TOKEN="**TU TWOJ TOKEN APLIKACJI DROPBOX**"
heroku config:set NOREPLY_ACCOUNT="twoj_adres@email.com"
heroku config:set NOREPLY_PASSWORD="magiczneHaslo"
heroku config:set NOREPLY_TARGET=""
heroku config:set RECAPTCHA_SITE_KEY=""
heroku config:set RECAPTCHA_SECRET_KEY=""
heroku config:set DEBUG=0
```
3. Wypychamy naszą aplikację na serwer heroku
```bash
git push heroku master
```
4. Upewniamy się, że wypchnięta przez nas instancja działa
```bash
heroku ps:scale web=1
```
5. Otwieramy strone apki
```bash
heroku open
```
6. W przypadku błędów sprawdzamy logi.
```bash
heroku logs --tail
```
