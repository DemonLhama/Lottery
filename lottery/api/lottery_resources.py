from flask_restful import Resource, reqparse
from lottery.db.models import UserTable, LotteryTable
from lottery.api.filters import *
from lottery.api.methods import user_not_exists

args = reqparse.RequestParser()
args.add_argument("email", type=str, required=True)

class Create_Game(Resource):
    def post(self):
        data = args.parse_args()

        if user_not_exists(data):
            user = UserTable(**data)
            user.create_user()

        lotto_numbers = LotteryTable.generate_lotto_ticket()
        game = LotteryTable(game_numbers=lotto_numbers, email=data.get('email'))
        try:
            game.save_lotto()
        except:
            return {"message": "Error"}, 500
        
        return game.json(), 201

