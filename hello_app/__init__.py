from flask import Flask  # Import the Flask class
app = Flask(__name__)    # Create an instance of the class for our use

from .db import create_db_command
app.cli.add_command(create_db_command)