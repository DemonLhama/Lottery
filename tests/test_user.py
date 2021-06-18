import requests
from lottery.db.models import UserTable
from lottery.db import db
from tests.util import body, headers


def test_request_get_email():
    respost = requests.request("GET", "http://127.0.0.1:5000/search", json=body, headers=headers)
    assert respost.status_code == 200


def test_post_email():
    respost = requests.request("POST", "http://127.0.0.1:5000/lottery", json=body, headers=headers)
    assert respost.status_code == 201
    assert respost.headers["Content-Type"] == "application/json"


def test_user_search(app):
    db.init_app(app)
    search = UserTable.find_user(body.get("email"))
    user = search.json()
    assert user["email"] == body.get("email")