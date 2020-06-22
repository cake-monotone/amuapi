from flask import Blueprint
from flask_restful import Resource, Api, fields
from flask_jwt_extended import (
    JWTManager,
    jwt_required,
    create_access_token,
    get_jwt_identity,
    get_raw_jwt,
    get_raw_jwt_header,
)

bp = Blueprint("numbaseball", __name__, url_prefix="/num-baseball")
api = Api(bp)


from . import start
from . import question

api.add_resource(start.Start, "/start")
api.add_resource(question.Question, "/question")

