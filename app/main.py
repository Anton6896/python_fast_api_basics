from typing import NoReturn, Optional
from fastapi import FastAPI, Depends

from app.schemas.blog_schema import BlogSchema
from app.user.models import User
from app.blog.models import Blog
from app.db.database import Base, get_db
from app.db.database import engine
from app.db.database import SessionLocal
from sqlalchemy.orm import Session

server = FastAPI()
Base.metadata.create_all(engine)  # ensure all tables


# ==============================================================  GET


@server.get("/")
def initial():
    return {"msg": "all blog list "}


@server.get("/blog/{id}")
def blog_id(id: int):
    return {"blog number ": f"{id}"}


@server.get("/blog/{id}/comment")
def blog_comments(id: int):
    return {'blog comment': f'comment for {id} blog'}


@server.get('/blog')
def blog_query(q: Optional[str] = None, limit: int = 10, publish: bool = True):
    if q:
        return {'blog query': f'query {q}'}
    else:
        return {'blog query': f'add "?q" for query'}


# ============================================================== POST


@server.post('/blog')
def create_blog(request: BlogSchema, db: Session = Depends(get_db)):
    new_blog = Blog(
        title=request.title,
        body=request.body,
    )

    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return {'OK': f'{new_blog}'}
