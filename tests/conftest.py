import os

import pytest


@pytest.fixture
def client():
    os.environ["FLASK_SECRET_KEY"] = "dev"
    os.environ["JWT_SECRET_KEY"] = "dev"
    os.environ["FLASK_ENV"] = "dev"

    from amuapi import app

    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client
