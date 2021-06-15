from flask import Flask
from lottery import config
from lottery import db
from lottery import cli
from lottery import api


def create_app():
    app = Flask(__name__)
    config.init_app(app)
    db.init_app(app)
    cli.init_app(app)
    api.init_app(app)
    return app
