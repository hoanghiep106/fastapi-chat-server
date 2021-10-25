from typing import List

from pydantic import BaseModel, constr

from main.schemas.pagination import PaginationModel


class AuthModel(BaseModel):
    name: constr(strip_whitespace=True, min_length=1)


class UserModel(BaseModel):
    id: str
    name: str


class UserPaginationModel(PaginationModel):
    items: List[UserModel]
