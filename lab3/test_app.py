#Author Hubert Wawszczak
from fastapi.testclient import TestClient
from unittest.mock import MagicMock
from lab3.main import app, get_db_connection

client = TestClient(app)

def override_get_db_connection():
    conn = MagicMock()
    conn.execute = MagicMock()
    return conn

app.dependency_overrides[get_db_connection] = override_get_db_connection

# Testy

def test_create_person_success():
    response = client.post("/people/", json={"first_name": "Jan", "last_name": "Kowalski"})
    assert response.status_code == 200

def test_create_person_invalid_data():
    response = client.post("/people/", json={"first_name": "Ja", "last_name": "Kowalski"})
    assert response.status_code == 422

def test_read_person_success():
    response = client.get("/people/1")
    assert response.status_code == 200

def test_read_person_not_found():
    response = client.get("/people/999")
    assert response.status_code == 404

def test_update_person_success():
    response = client.put("/people/1", json={"first_name": "Jan", "last_name": "Nowak"})
    assert response.status_code == 200

def test_update_person_not_found():
    response = client.put("/people/999", json={"first_name": "Jan", "last_name": "Nowak"})
    assert response.status_code == 404

def test_delete_person_success():
    response = client.delete("/people/1")
    assert response.status_code == 200

def test_delete_person_not_found():
    response = client.delete("/people/999")
    assert response.status_code == 404

def test_read_all_persons():
    response = client.get("/people/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_person_invalid_id():
    response = client.get("/people/abc")
    assert response.status_code == 422

# Uwaga: Testy mogą wymagać dostosowania do specyfiki Twojej aplikacji.
