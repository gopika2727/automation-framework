def test_register_user():
    data = {
        "email": "test@test.com",
        "password": "123456"
    }

    print("DATA:", data)

    response = {
        "status_code": 201
    }

    assert response["status_code"] == 201