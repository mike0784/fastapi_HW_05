from typing import Optional
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    status: bool

class Id(BaseModel):
    id: int