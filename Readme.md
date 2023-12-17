# Projekt Flask Greetings - Przykładowe Testy

Projekt Flask Greetings to prosta aplikacja webowa, która umożliwia użytkownikom wprowadzanie swojego imienia, a następnie wyświetla przywitanie na stronie. Ten plik `readme.md` zawiera przykłady testów jednostkowych oraz testów interfejsu użytkownika (UI) przeprowadzanych w ramach tego projektu.

## Wymagania

Aby uruchomić testy, upewnij się, że masz zainstalowane następujące zależności:

- Python 3.11
- Flask
- Flask-SQLAlchemy
- Selenium
- Inne zależności z pliku `requirements.txt`

## Struktura projektu

- `app.py`: Główny plik aplikacji Flask.
- `test_gui.py`: Testy interfejsu użytkownika przy użyciu Selenium.
- `test_app.py`: Testy jednostkowe aplikacji.
- `templates/`: Szablony HTML używane przez aplikację.
- `greetings.db`: Baza danych SQLite przechowująca przywitania.

## Funkcje

- Użytkownicy mogą wprowadzić swoje imię i zatwierdzić je.
- Aplikacja wyświetli przywitanie na stronie głównej.
- Możliwość wyświetlenia listy wcześniejszych przywitaniach na stronie "/greetings".

## Instalacja

1. Sklonuj repozytorium na swój lokalny komputer:
`git clone https://github.com/Hubert-Wawszczak/Testy_selenium_pytest.git`

2. Przejdź do katalogu projektu:

3. Zainstaluj zależności przy użyciu `pip`:

`pip install -r requirements.txt`


## Uruchomienie

Aby uruchomić aplikację, użyj poniższej komendy:

`python app.py`

## Uruchamianie Testów

### Testy Jednostkowe

Testy jednostkowe sprawdzają pojedyncze komponenty aplikacji. Aby uruchomić testy jednostkowe, użyj poniższej komendy:


### Testy Interfejsu Użytkownika (UI)

Testy interfejsu użytkownika (UI) sprawdzają interakcje użytkownika z aplikacją w przeglądarce. Aby uruchomić testy UI, użyj poniższej komendy:


## Przykładowe Testy

Oto kilka przykładowych testów jednostkowych i testów UI:

### Testy Jednostkowe (`test_app.py`)

1. Test dodawania przywitania do bazy danych:

```python
def test_greeting(test_client):
    response = test_client.post('/greet', data={'name': 'Test User'})
    assert response.status_code == 200
    with app.app_context():
        assert Greeting.query.filter_by(name='Test User').first() is not None

Autor
Hubert Wawszczak

Ten `readme.md` zawiera przykłady testów jednostkowych i testów interfejsu użytkownika (UI) oraz opisuje, jak uruchomić te testy w ramach projektu Flask Greetings. Upewnij się, że dostosujesz informacje takie jak autor, URL repozytorium, i inne szczegóły projektu do swoich potrzeb.
