import sqlite3
from flask_restful import Resource, reqparse
from lottery.api.filters import *

args = reqparse.RequestParser()
args.add_argument("email", type=str, required=True)

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