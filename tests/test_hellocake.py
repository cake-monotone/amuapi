import pytest


def test_hellocake(client):
    """
    Hello, World 테스트
    """
    response = client.get("/hello-cake/cake")
    assert response.status_code == 200
    assert response.is_json

    data = response.get_json()

    assert data == {"cake": "Red Velvet", "msg": "Hello! It's my favorite cake!"}

