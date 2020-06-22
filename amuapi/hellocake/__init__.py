from flask import Blueprint, make_response
from flask_restful import Resource, Api

bp = Blueprint("hellocake", __name__, url_prefix="/hello-cake")
api = Api(bp)


class Cake(Resource):
    def get(self):
        return {
            "msg": "Hello! It's my favorite cake!",
            "cake": "Red Velvet",
        }


class TeaPot(Resource):
    def get(self):
        return make_response("먼걸음을 달려와주셔서 정말 감사하지만, 전 혼자 있고 싶어요..", 418)


api.add_resource(Cake, "/cake")
api.add_resource(TeaPot, "/teapot")

