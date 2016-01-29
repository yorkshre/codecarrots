### Dokumentacja aplikacji przygotowanej na potrzeby konferencji codecarrots w Koszalinie
### 
#### Konfiguracja deweloperska:
###### 1. Szykujemy virtualenva w wersji pythona 3.4 
###### 2. Musimy posiadać konto w serwisie dropbox. Tworzymy nową aplikację https://www.dropbox.com/developers/apps/create, najlepiej z dedykowanym folderem. Klikamy "Generate acccess token". Przyjmując, że nasz wirtualenv jest w folderze .venv konfigurujemy skyrpt .venv/bin/activate, 
dodajemy wpis:
```bash
DROPBOX_OAUTH2_TOKEN = "**TU TWOJ TOKEN APLIKACJI DROPBOX**" 
export DROPBOX_OAUTH2_TOKEN
```
###### 3. Tworzymy pustą bazę sqllite i migrujemy modele.
###### 4. Uruchamiamy aplikację.

##### Uwagi:
###### Pliki wrzucane do bazy w administracji aplikacji wrzucane sa produkcyjne na moje (lukasz zielinski) konto dropboksa. Klucz znajduje sie w konfiguracji aplikacji na heroku


