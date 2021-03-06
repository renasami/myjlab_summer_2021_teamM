
# from app.python.models.schemas import Users

from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from starlette.middleware.cors import CORSMiddleware

import models.dbSchemas  as md
from models.database import ENGINE

import auth
from routers import posts, reactions,users,tests 

origins = [
    "http://127.0.0.1:8080",
    "*"
]

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins= origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(auth.router, prefix="/auth")
app.include_router(posts.router, prefix="/posts")
app.include_router(reactions.router, prefix="/reactions")
app.include_router(users.router, prefix="/users")
app.include_router(tests.router, prefix="/tests")

md.Base.metadata.create_all(bind=ENGINE)
clients = {}

# テスト用のtemplates指定
templates = Jinja2Templates(directory="./templates")






if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)