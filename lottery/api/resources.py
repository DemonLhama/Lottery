import sqlite3
from flask_restful import Resource, reqparse
from lottery.db.models import UserTable, LotteryTable
from lottery.api.filters import *

args = reqparse.RequestParser()
args.add_argument("email", type=str, required=True)

class Create_Game(Resource):
    def post(self):
        data = args.parse_args()

        if not UserTable.find_user(data.get("email")):
            user = UserTable(**data)
            user.create_user()

        lotto_numbers = LotteryTable.generate_lotto_ticket()
        game = LotteryTable(game_numbers=lotto_numbers, email=data.get('email'))
        try:
            game.save_lotto()
        except:
            return {"message": "Error"}, 500
        
        return game.json(), 201



class FindUser(Resource):
    def get(self):
        connection = sqlite3.connect("lottery/lottery.db")
        cursor = connection.cursor()
        data = args.parse_args()
        valid_data = {key:data[key] for key in data if data[key] is not None}
        data = search_normalize(**valid_data)
        tupla = tuple([data[keys] for keys in data])

        if data.get('email'):
            result = cursor.execute(email_consult, tupla)

        user = []
        for line in result :
            user.append({
                "lotto_id": line[0],
                "game_numbers": line[1]
            })

        return {"The user {}, has this lottery tickets".format(data.get('email')): user}