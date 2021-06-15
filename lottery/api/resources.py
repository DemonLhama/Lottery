import sqlite3
from random import randint
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
        
        a = randint(1,60)
        b = randint(1,60)
        c = randint(1,60)
        d = randint(1,60)
        e = randint(1,60)
        f = randint(1,60)
        g = randint(1,60)
        h = randint(1,60)
        i = randint(1,60)
        j = randint(1,60)
        lotto_numbers = "{},{},{},{},{},{},{},{},{},{}".format(a,b,c,d,e,f,g,h,i,j)
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