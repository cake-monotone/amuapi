from flask_jwt_extended import decode_token


def test_start(client):
    response = client.post("/num-baseball/start", data={})

    assert response.status_code == 200
    assert response.is_json

    data = response.get_json()
    assert "access_token" in data


def test_start_with_wrong_parameter(client):
    """
    잘못된 파라미터 테스트
    """

    # range digit 테스트
    response = client.post("/num-baseball/start", data={"range_digit": -1})
    assert response.status_code == 400
    assert b"Invalid value" in response.data and b"range_digit" in response.data

    response = client.post("/num-baseball/start", data={"num_digit": -1})
    assert response.status_code == 400
    assert b"Invalid value" in response.data and b"num_digit" in response.data

    # num_digit <= range_digit 테스트
    response = client.post(
        "/num-baseball/start", data={"num_digit": 5, "range_digit": 3}
    )
    assert response.status_code == 400
    assert (
        b"Invalid value" in response.data
        and b"num_digit" in response.data
        and b"range_digit" in response.data
    )

    # 잘못된 파라미터
    response = client.post("/num-baseball/start", data={"range_digit": "string"})
    assert response.status_code == 400


def get_token(client, range_digit, num_digit):
    response = client.post(
        "/num-baseball/start", data={"range_digit": range_digit, "num_digit": num_digit}
    )
    return response.get_json()["access_token"]


def test_question(client):
    token = get_token(client, 9, 3)
    data = decode_token(token)

    response = client.post(
        "/num-baseball/question",
        data={"answer": [1, 2, 3]},
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == 200
    assert b"strikes" in response.data
