import json
from typing import List

from starlette.websockets import WebSocket


class ChatRoom:
    def __init__(self):
        self.clients: List[WebSocket] = []

    async def connect(self, client: WebSocket):
        await client.accept()
        self.clients.append(client)

    async def broadcast(self, sender_id: int, message: str):
        text = json.dumps({
            "sender_id": sender_id,
            "message": message
        })
        for client in self.clients:
            await client.send_text(text)
