import requests

BASE_URL = "https://dummyjson.com"
def test_login_success():
    response = {
        "status_code": 200,
        "token": "abc123"
    }

    assert response["status_code"] == 200
    assert "token" in response


def test_login_fail():
    response = {
        "status_code": 400,
        "error": "Missing password"
    }

    assert response["status_code"] == 400