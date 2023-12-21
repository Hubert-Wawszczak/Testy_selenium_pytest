
from database import get_db_connection
from models import Person
from fastapi import HTTPException

def create_person(person: Person):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO people (first_name, last_name) VALUES (?, ?)',
                   (person.first_name, person.last_name))
    conn.commit()
    person.id = cursor.lastrowid
    conn.close()
    return person

def read_person(person_id: int):
    conn = get_db_connection()
    person = conn.execute('SELECT * FROM people WHERE id = ?', (person_id,)).fetchone()
    conn.close()
    if person is None:
        raise HTTPException(status_code=404, detail="Person not found")
    return person

def update_person(person_id: int, updated_person: Person):
    conn = get_db_connection()
    conn.execute('UPDATE people SET first_name = ?, last_name = ? WHERE id = ?',
                 (updated_person.first_name, updated_person.last_name, person_id))
    conn.commit()
    conn.close()
    return updated_person

def delete_person(person_id: int):
    conn = get_db_connection()
    person = conn.execute('SELECT * FROM people WHERE id = ?', (person_id,)).fetchone()
    if person is None:
        raise HTTPException(status_code=404, detail="Person not found")
    conn.execute('DELETE FROM people WHERE id = ?', (person_id,))
    conn.commit()
    conn.close()
    return person
