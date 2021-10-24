from typing import TypedDict

from bson import ObjectId


class DocT(TypedDict):
    _id: ObjectId


class UserDocT(DocT):
    name: str
