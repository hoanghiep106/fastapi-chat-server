from datetime import datetime

from starlette.websockets import WebSocket, WebSocketDisconnect

from main import app, chat_room, logger
from main.schemas.message import MessageModel
from main.services import message as message_service
from main.services import user as user_service


@app.websocket("/chat/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: str):
    user_doc = await user_service.get_user(user_id)
    if not user_doc:
        logger.info(f"User {user_id} not found")
        await websocket.close()
        return

    await chat_room.connect(websocket)
    try:
        while True:
            content = await websocket.receive_text()
            message = _construct_message(user_id, content)
            await chat_room.broadcast(message)
            await message_service.create_message(message)
    except WebSocketDisconnect:
        logger.info(f"User {user_id} disconnected")
        chat_room.disconnect(websocket)


def _construct_message(user_id: str, content: str) -> MessageModel:
    return MessageModel(
        user_id=user_id,
        content=content,
        created_at=datetime.utcnow().isoformat()
    )
