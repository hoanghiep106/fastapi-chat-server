from datetime import datetime
from typing import TypedDict

from bson import ObjectId


class DocT(TypedDict):
    _id: ObjectId


class UserDocT(DocT):
    name: str


class MessageDocT(DocT):
    user_id: str
    content: str
    created_at: datetime
