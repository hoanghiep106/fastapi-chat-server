import requests

from main.schemas.user import UserModel
from tests.constants import API_SERVER_URL

current_user_index = 0


def get_new_user_name():
    global current_user_index
    current_user_index += 1
    return f"User {current_user_index}"


class TestAuth:
    base_url = API_SERVER_URL

    def test_sign_up_failed(self):
        response = requests.post(f"{self.base_url}/auth", json={"name": None})
        assert response.status_code == 422

        response = requests.post(f"{self.base_url}/auth", json={"name": ""})
        assert response.status_code == 422

        response = requests.post(f"{self.base_url}/auth", json={"name": "   "})
        assert response.status_code == 422

    def test_sign_up_successfully(self):
        response = requests.post(f"{self.base_url}/auth", json={"name": get_new_user_name()})
        assert response.status_code == 200
        user = response.json()
        assert UserModel.validate(user)

    def test_sign_in_successfully(self):
        name = get_new_user_name()
        # Sign up
        response = requests.post(f"{self.base_url}/auth", json={"name": name})
        assert response.status_code == 200
        user_id = response.json()["id"]
        # Sign in
        response = requests.post(f"{self.base_url}/auth", json={"name": name})
        assert response.status_code == 200
        assert user_id == response.json()["id"]
