from flask_restful import Api
from flask import Blueprint
from lottery.api.resources import Create_Game, FindUser

api_bp = Blueprint("api", __name__)
api = Api(api_bp)


api.add_resource(Create_Game, "/lottery")
api.add_resource(FindUser, "/search")