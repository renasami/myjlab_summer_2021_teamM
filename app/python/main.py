
# from app.python.models.schemas import Users

from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from starlette.middleware.cors import CORSMiddleware

from models import tasks   #テーブル作成したら随時追加
from models.database import ENGINE

import auth
from routers import posts, reactions,users 

app=FastAPI()

app.include_router(auth.router, prefix="/auth")
app.include_router(posts.router, prefix="/posts")
app.include_router(reactions.router, prefix="/reactions")
app.include_router(users.router, prefix="/users")

tasks.Base.metadata.create_all(bind=ENGINE)
clients = {}

# テスト用のtemplates指定
templates = Jinja2Templates(directory="templates")



origins = [
    "http://localhost:8080",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins= origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)



if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)