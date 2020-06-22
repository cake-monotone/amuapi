from flask import make_response, jsonify
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_claims

parser = reqparse.RequestParser()
parser.add_argument("answer", type=int, action="append", required=True)


class Question(Resource):
    @jwt_required
    def post(self):
        """
        답을 검증하고 돌려줍니다.
        """
        req_data = parser.parse_args()
        game_data = get_jwt_claims()
        answer_array = req_data["answer"]

        # 예외 처리
        if (
            "game_array" not in game_data
            and "num_digit" not in game_data
            and "range_digit" not in game_data
        ):
            return make_response(jsonify(message="Invalid access token"), 400)

        if len(answer_array) != game_data["num_digit"]:
            return make_response(
                jsonify(message="Invalid answer : wrong length of answer"), 400
            )

        # 스트라이크, 볼 개수 세기
        game_array = game_data["game_array"]
        rest_set = set()

        strikes = 0
        balls = 0

        for A, B in zip(answer_array, game_array):
            if A == B:
                strikes += 1
            else:
                rest_set.add(B)

        for val in answer_array:
            if val in rest_set:
                balls += 1

        return make_response(
            jsonify(strikes=strikes, balls=balls, num_digit=game_data["num_digit"]), 200
        )

