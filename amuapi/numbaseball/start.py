import random

from flask import make_response, jsonify
from flask_restful import reqparse, Resource
from flask_jwt_extended import JWTManager, create_access_token

parser = reqparse.RequestParser()
parser.add_argument("range_digit", type=int)
parser.add_argument("num_digit", type=int)

# Default Value
RANGE_DIGIT_DEFAULT = 9
NUM_DIGIT_DEFAULT = 3

MAX_LIM_RANGE = 1000000
MAX_LIM_NUM = 1000


class Start(Resource):
    def post(self):
        """
        숫자 야구 게임을 생성하고 해당 상태를 access_token으로 만들어
        반환합니다.
        """
        args = parser.parse_args()
        range_digit = args["range_digit"]
        num_digit = args["num_digit"]

        if not range_digit:  # DEFAULT_VALUE
            range_digit = RANGE_DIGIT_DEFAULT
        if not num_digit:
            num_digit = NUM_DIGIT_DEFAULT

        # 입력값 체크
        err_str = None
        if not (1 <= range_digit <= MAX_LIM_RANGE):
            err_str = f"Invalid value : range_digit should be 1 <= range_digit <= {MAX_LIM_RANGE}"
        elif not (1 <= num_digit <= MAX_LIM_NUM):
            err_str = (
                f"Invalid value : num_digit should be 1 <= num_digit <= {MAX_LIM_NUM}"
            )
        elif not (num_digit <= range_digit):
            err_str = "Invalid value : num_digit <= range_digit"

        if err_str:
            return make_response(jsonify(message=err_str), 400)

        # 게임 생성
        game_array = random.sample(range(1, range_digit + 1), num_digit)

        access_token = create_access_token(
            "",
            user_claims={
                "game_array": game_array,
                "range_digit": range_digit,
                "num_digit": num_digit,
            },
        )

        return make_response(jsonify(access_token=access_token), 200)

