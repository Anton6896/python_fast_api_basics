from typing import NoReturn, Optional

from fastapi import FastAPI

server = FastAPI()


@server.get("/")
def initial():
    return {"msg": "all blog list "}


@server.get('/blog')
def blog_query(q: Optional[str] = None):
    if q:
        return {'blog query': f'query {q}'}
    else:
        return {'blog query': f'add "?q" for query'}


@server.get("blog/{id}")
def blog_id(id: int):
    return {"blog number ": f"{id}"}


@server.get("/blog/{id}/comment")
def blog_comments(id: int):
    return {'blog comment': f'comment for {id} blog'}


# @server.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}
