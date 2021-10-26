from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel, constr

from main.schemas.pagination import PaginationModel
from main.schemas.user import UserModel


class MessageModel(BaseModel):
    id: Optional[str]
    user: UserModel
    content: constr(strip_whitespace=True, min_length=1, max_length=1000)
    created_at: datetime


class MessagePaginationModel(PaginationModel):
    items: List[MessageModel]
