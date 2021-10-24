from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel

from main.schemas.pagination import PaginationModel


class MessageModel(BaseModel):
    id: Optional[str]
    user_id: str
    content: str
    created_at: datetime


class MessagePaginationModel(PaginationModel):
    items: List[MessageModel]
