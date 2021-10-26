import requests

from main import config
from main.schemas.pagination import PaginationModel
from tests.constants import API_SERVER_URL


class TestUser:
    base_url = API_SERVER_URL

    def test_get_users(self):
        response = requests.get(f"{self.base_url}/users")
        assert response.status_code == 200
        data = response.json()
        assert PaginationModel.validate(data)
        if data["total"] >= config.DEFAULT_PAGE_LIMIT:
            assert len(data["items"]) == config.DEFAULT_PAGE_LIMIT
        else:
            assert data["total"] == len(data["items"])
