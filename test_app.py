import pytest
from app import app, db, Greeting

@pytest.fixture(scope="module")
def test_client():
    flask_app = app

    # Konfiguracja aplikacji do testowania
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    flask_app.config['TESTING'] = True

    # Utworzenie kontekstu aplikacji
    with flask_app.app_context():
        db.create_all()

    # Utworzenie testowego klienta
    testing_client = flask_app.test_client()

    # Kontekst jest aktywny dla całego czasu trwania testów w tym module
    yield testing_client

    # Usunięcie danych po zakończeniu testów
    with flask_app.app_context():
        db.drop_all()

def test_greeting(test_client):
    # Testowanie endpointu
    response = test_client.post('/greet', data={'name': 'Test User'})
    assert response.status_code == 200

    # Sprawdzenie czy dane są w bazie danych
    with app.app_context():
        assert Greeting.query.filter_by(name='Test User').first() is not None

def test_greeting_no_data(test_client):
    response = test_client.post('/greet')
    assert response.status_code == 200
    assert b"Hello, World!" in response.data

def test_greeting_invalid_data(test_client):
    response = test_client.post('/greet', data={'name': ''})
    assert response.status_code == 200
    assert b"Hello, !" in response.data  # Update this line to check for the correct response





# Test dla tego endpointu
def test_show_greetings(test_client):
    response = test_client.get('/greetings')
    assert response.status_code == 200
    assert b"List of Greetings" in response.data  # Zakładając, że strona zawiera taki tekst


def test_database_interaction(test_client):
    test_client.post('/greet', data={'name': 'Unique User'})
    with app.app_context():
        greeting = Greeting.query.filter_by(name='Unique User').first()
        assert greeting is not None
        assert greeting.name == 'Unique User'
