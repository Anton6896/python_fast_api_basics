from re import VERBOSE
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from datetime import datetime
from sqlalchemy.orm import relationship

from app.db.database import Base


class Blog(Base):
    __tablename__ = 'blogs'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True)
    body = Column(String)
    is_active = Column(Boolean, default=True)
    published: Column(Boolean, default=True)
    created_at: Column(DateTime, default=datetime.now())

    created_by: relationship("User", back_populates="blogs")
