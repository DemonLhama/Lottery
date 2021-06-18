import pytest
from lottery.app import create_app
from lottery.db import db
from tests.util import body
from lottery.db.models import UserTable



@pytest.fixture(scope="module")
def app():
    """ Instance of Main flask app """
    app = create_app()
    return app

