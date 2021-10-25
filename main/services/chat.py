from typing import List

from starlette.websockets import WebSocket

from main.schemas.message import MessageModel


class ChatRoom:
    def __init__(self):
        self.clients: List[WebSocket] = []

    async def connect(self, client: WebSocket):
        await client.accept()
        self.clients.append(client)

    def disconnect(self, websocket: WebSocket):
        self.clients.remove(websocket)

    async def broadcast(self, message: MessageModel):
        text = message.json()
        for client in self.clients:
            await client.send_text(text)
