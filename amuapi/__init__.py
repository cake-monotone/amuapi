import os

from flask import Flask
from flask_jwt_extended import JWTManager


def create_app(**config):
    """
    앱 생성 및 설정
    """
    app = Flask(__name__)
    app.config.from_mapping(**config)

    # 블루 프린트 설정
    from . import hellocake
    from . import numbaseball

    app.register_blueprint(hellocake.bp)
    app.register_blueprint(numbaseball.bp)

    return app


def get_configs_from_env():
    if "JWT_SECRET_KEY" not in os.environ:
        raise RuntimeError('No "JWT_SECRET_KEY" variable in environ.')
    if "FLASK_SECRET_KEY" not in os.environ:
        raise RuntimeError('No "FLASK_SECRET_KEY" variable in environ.')

    return {
        "JWT_SECRET_KEY": os.environ["JWT_SECRET_KEY"],
        "SECRET_KEY": os.environ["FLASK_SECRET_KEY"],
    }


configs = get_configs_from_env()

app = create_app(**configs)
jwt = JWTManager(app)

