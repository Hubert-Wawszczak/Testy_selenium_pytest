import pytest
from app import app, db, Greeting

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    client = app.test_client()

    with app.app_context():
        db.create_all()

    yield client

    with app.app_context():
        db.drop_all()

def test_home_page_loads(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Enter your name' in response.data  # Zakładając, że formularz zawiera ten tekst

def test_create_greeting(client):
    response = client.post('/greet', data={'name': 'Flask Tester'})
    assert response.status_code == 200
    assert b'Hello, Flask Tester!' in response.data

    with app.app_context():
        greeting = Greeting.query.filter_by(name='Flask Tester').first()
        assert greeting is not None
        assert greeting.name == 'Flask Tester'

def test_show_all_greetings(client):
    # Dodajemy dwa pozdrowienia do bazy danych
    with app.app_context():
        db.session.add(Greeting(name="Tester One"))
        db.session.add(Greeting(name="Tester Two"))
        db.session.commit()

    response = client.get('/greetings')
    assert response.status_code == 200
    assert b'Tester One' in response.data
    assert b'Tester Two' in response.data


def test_update_greeting(client):
    with app.app_context():  # Umieszczenie operacji w kontekście aplikacji
        # Najpierw dodajemy nowe pozdrowienie
        new_greeting = Greeting(name="Update Test")
        db.session.add(new_greeting)
        db.session.commit()

        updated_name = "Updated Name"
        response = client.put(f'/greeting/{new_greeting.id}', data={'name': updated_name})
        assert response.status_code == 200

        # Sprawdzenie, czy nazwa pozdrowienia została zaktualizowana
        updated_greeting = Greeting.query.get(new_greeting.id)
        assert updated_greeting.name == updated_name


def test_update_greeting2(client):
    with app.app_context():  # Umieszczenie operacji w kontekście aplikacji
        # Dodajemy nowe pozdrowienie
        new_greeting = Greeting(name="Update Test")
        db.session.add(new_greeting)
        db.session.commit()

        updated_name = "Updated Name"
        response = client.put(f'/greeting/{new_greeting.id}', data={'name': updated_name})
        assert response.status_code == 200

        # Sprawdzamy, czy nazwa pozdrowienia została zaktualizowana
        updated_greeting = db.session.get(Greeting, new_greeting.id)
        assert updated_greeting.name == updated_name

def test_delete_greeting(client):
    with app.app_context():  # Umieszczenie operacji w kontekście aplikacji
        # Najpierw dodajemy nowe pozdrowienie
        new_greeting = Greeting(name="Delete Test")
        db.session.add(new_greeting)
        db.session.commit()

        response = client.delete(f'/greeting/{new_greeting.id}')
        assert response.status_code == 200

        # Sprawdzenie, czy pozdrowienie zostało usunięte
        deleted_greeting = db.session.get(Greeting, new_greeting.id)  # Używamy db.session.get()
        assert deleted_greeting is None
