
from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class UserSchema(BaseModel):
    name: str


class BlogSchema(BaseModel):
    title: str
    body: str
    published: Optional[bool]
    created_by: UserSchema
    created_at: datetime
