import sqlite3
import click
from flask import current_app
from flask.cli import with_appcontext


def get_db():
    return sqlite3.connect('hikes.db')


# commandolinje i (.env) flask_tutorial_22 katalogen: flask --app hello_app create-db
@click.command('create-db')
@with_appcontext
def create_db_command():
    db = get_db()
    f = current_app.open_resource('script/schema.sql')
    db.executescript(f.read().decode('utf8'))
    f.close()



