from typing import List, Any

from pydantic import BaseModel


class PaginationModel(BaseModel):
    items: List[Any]
    limit: int
    skip: int
    total: int
