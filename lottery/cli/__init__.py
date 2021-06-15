from lottery.db import db
from lottery.db.models import *

def init_app(app):
    # Using the cli command you can create the db using the command flask create-db.
    @app.cli.command()
    def create_db():
        "Initialize the database"
        db.create_all()