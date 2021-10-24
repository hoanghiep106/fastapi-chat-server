from starlette.websockets import WebSocket

from main import app, chat_room
from main.services.message import create_message, construct_message


@app.websocket("/chat/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: str):
    await chat_room.connect(websocket)
    while True:
        content = await websocket.receive_text()
        message = construct_message(user_id, content)
        await chat_room.broadcast(message)
        await create_message(message)
