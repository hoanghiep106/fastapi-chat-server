from typing import List

from pydantic import BaseModel

from main.schemas.pagination import PaginationModel


class AuthModel(BaseModel):
    name: str


class UserModel(BaseModel):
    id: str
    name: str


class UserPaginationModel(PaginationModel):
    items: List[UserModel]
