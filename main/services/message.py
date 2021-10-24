from datetime import datetime
from typing import Awaitable, List

from main.database import message_collection
from main.schemas.message import MessageModel
from main.types import MessageDocT


def construct_message(user_id: str, content: str) -> MessageModel:
    return MessageModel(
        user_id=user_id,
        content=content,
        created_at=datetime.utcnow().isoformat()
    )


async def create_message(message: MessageModel) -> Awaitable[MessageDocT]:
    message_doc = await message_collection.insert_one(message.dict())
    return message_collection.find_one({"_id": message_doc.inserted_id})


async def get_messages(skip: int, limit: int, sort: str = None) -> List[MessageDocT]:
    cursor = message_collection.find({})
    if sort:
        sort_order = 1
        if sort.startswith("-"):
            sort_order = -1
            sort = sort[1:]
        cursor.sort(sort, sort_order)
    cursor.skip(skip).limit(limit)
    message_docs = []
    async for doc in cursor:
        message_docs.append(doc)
    return message_docs


def count_messages() -> Awaitable[int]:
    return message_collection.count_documents({})
