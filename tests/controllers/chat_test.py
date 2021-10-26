import json

import pytest
import requests
from bson import ObjectId
from websocket import create_connection, WebSocketBadStatusException

from tests.constants import WEBSOCKET_SERVER_URL, API_SERVER_URL


class TestChat:
    api_url: str = API_SERVER_URL
    websocket_url: str = WEBSOCKET_SERVER_URL

    def _setup(self):
        self.users = []
        for i in range(0, 2):
            response_1 = requests.post(f"{self.api_url}/auth", json={"name": f"Chat user {i + 1}"})
            self.users.append(response_1.json())

    def test_invalid_user_id(self):
        # Invalid BSON ID
        invalid_id = "abcd"
        with pytest.raises(WebSocketBadStatusException):
            create_connection(f"{self.websocket_url}/chat/{invalid_id}")

        # Not found user ID
        not_existed_id = str(ObjectId())
        with pytest.raises(WebSocketBadStatusException):
            create_connection(f"{self.websocket_url}/chat/{not_existed_id}")

    def test_connect_successfully(self):
        self._setup()
        create_connection(f"{self.websocket_url}/chat/{self.users[0]['id']}")

    def test_send_message_successfully(self):
        self._setup()
        websocket_1 = create_connection(f"{self.websocket_url}/chat/{self.users[0]['id']}")
        websocket_2 = create_connection(f"{self.websocket_url}/chat/{self.users[1]['id']}")

        content = "Hello, World"
        websocket_1.send(content)
        data = json.loads(websocket_2.recv())
        assert data["user"] == {
            "id": self.users[0]["id"],
            "name": self.users[0]["name"]
        }
        assert data["content"] == content
