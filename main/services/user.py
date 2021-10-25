import asyncio
from typing import Awaitable, List, Optional

from bson import ObjectId
from bson.errors import InvalidId

from main.database import user_collection
from main.schemas.user import AuthModel
from main.types import UserDocT


async def create_user(user: AuthModel) -> Awaitable[UserDocT]:
    user_doc = await user_collection.insert_one(user.dict())
    return await user_collection.find_one({"_id": user_doc.inserted_id})


async def get_users(skip: int, limit: int) -> List[UserDocT]:
    cursor = user_collection.find({}).skip(skip).limit(limit)
    user_docs = []
    async for doc in cursor:
        user_docs.append(doc)
    return user_docs


def count_users() -> Awaitable[int]:
    return user_collection.count_documents({})


def get_user_by_name(name: str) -> Awaitable[Optional[UserDocT]]:
    return user_collection.find_one({"name": name})


def get_user(id: str) -> Awaitable[Optional[UserDocT]]:
    try:
        return user_collection.find_one({"_id": ObjectId(id)})
    except InvalidId:
        return asyncio.sleep(0, None)
