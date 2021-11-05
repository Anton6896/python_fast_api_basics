
from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class User(BaseModel):
    username: str


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]
    created_by: User
    created_at: datetime
