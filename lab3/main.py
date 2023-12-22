#Author Hubert Wawszczak

from fastapi import FastAPI
from lab3.crud import create_person, read_person, update_person, delete_person
from lab3.models import Person
from lab3.database import get_db_connection
import uvicorn

app = FastAPI()

@app.on_event("startup")
async def startup():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS people (
            id INTEGER PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.post("/people/", response_model=Person)
async def api_create_person(person: Person):
    return create_person(person)

@app.get("/people/{person_id}", response_model=Person)
async def api_read_person(person_id: int):
    return read_person(person_id)

@app.put("/people/{person_id}", response_model=Person)
async def api_update_person(person_id: int, updated_person: Person):
    return update_person(person_id, updated_person)

@app.delete("/people/{person_id}", response_model=Person)
async def api_delete_person(person_id: int):
    return delete_person(person_id)

if __name__ == "__main__":
    uvicorn.run(app, port=8000)
