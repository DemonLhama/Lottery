from lottery.db.models import LotteryTable
from lottery.db import db
from tests.util import lottery_ticket


def test_ticket_methods(app):
    db.init_app(app)
    lotto = LotteryTable.generate_lotto_ticket()
    assert len(lotto.split()) == 10


def test_class_create_game(app):
    db.init_app(app)
    game = LotteryTable(game_numbers=lottery_ticket.get("game_numbers"), email=lottery_ticket.get('email'))
    ticket = game.json()
    assert ticket["email"] == lottery_ticket.get("email")
    assert ticket["game_numbers"] == lottery_ticket.get("game_numbers")



