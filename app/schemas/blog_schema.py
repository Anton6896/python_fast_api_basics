
from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class BlogSchema(BaseModel):
    title: str
    body: str
