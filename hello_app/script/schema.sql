CREATE TABLE users (
    id integer PRIMARY KEY, 
    name text, 
    password text,
    email text,
    birth_date text,
    created_on text
    )
;

CREATE TABLE trips (
    id integer PRIMARY KEY, 
    user_id integer, 
    visit_date text,
    destination text,
    start_place text,
    created_on text
    )
;
