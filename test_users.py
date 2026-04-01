import requests
from utils.config import BASE_URL

def test_get_users():
    response = requests.get(f"{BASE_URL}/users")

    assert response.status_code == 200
    assert "users" in response.json()
    assert response.elapsed.total_seconds() < 2