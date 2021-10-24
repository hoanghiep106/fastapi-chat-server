from starlette.websockets import WebSocket

from main import app, chat_room


@app.websocket("/chat/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: int):
    await chat_room.connect(websocket)
    while True:
        message = await websocket.receive_text()
        await chat_room.broadcast(user_id, message)
