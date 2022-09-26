from datetime import datetime
import sqlite3

db = sqlite3.connect('hikes.db')
c = db.cursor()

q = """
CREATE TABLE users (
    id integer PRIMARY KEY, 
    name text, 
    password text,
    email text,
    birth_date text,
    created_on text
    )
"""
# Lager tabellen
#c.execute(q)


q = """
INSERT INTO users ( password, email, birth_date, created_on, name)
VALUES ('BBB', 'tom@test.no', '1971-02-28', '2022-09-26', 'Tom')
"""
# Setter inn data i tabellen - direkte
#c.execute(q)


q = """
INSERT INTO users (name, password, email, birth_date, created_on)
VALUES (?, ?, ?, ?, ?)
"""

entities = ('Tom', '*****', 'tom@test.no', '1971-02-28', datetime.now())

# Setter inn data i tabellen - med parameter
#c.execute(q, entities)

# TODO: Lag tabellen for trips og sett inn litt data



q = """
CREATE TABLE trips (
    id integer PRIMARY KEY, 
    user_id integer, 
    visit_date text,
    destination text,
    start_place text,
    created_on text
    )

"""
#c.execute(q)

q = """
INSERT INTO trips (user_id, visit_date, destination, start_place, created_on)
VALUES (?, ?, ?, ?, ?)
"""

entities = (1, '2022-09-26', 'Vestre vealøs', 'Skifjell', datetime.now())


c.execute(q, entities)

db.commit()
