
# from app.python.models.schemas import Users
from tempfile import NamedTemporaryFile
from typing import Optional
from starlette.websockets import WebSocket
from starlette import status

from fastapi import FastAPI, Depends, HTTPException, Request, File, UploadFile, Cookie
from fastapi.responses import HTMLResponse, ORJSONResponse, RedirectResponse, FileResponse
from fastapi.templating import Jinja2Templates
from starlette.status import HTTP_302_FOUND
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from datetime import datetime, timedelta

from models import crud, tasks, schemas, comments, likes, posts, users   #テーブル作成したら随時追加
from models.crud import try_login as crud_try_login
from models.database import session, ENGINE

from models.fromFrontClasses import LoginUserInfo
import os, re, ast, cv2, shutil, qrcode
from typing import Optional
from fastapi.security import APIKeyCookie
import time
import auth


# from starlette.middleware.sessions import SessionMiddleware
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
# import auth

app=FastAPI()

app.include_router(auth.router, prefix="/auth")

tasks.Base.metadata.create_all(bind=ENGINE)
clients = {}

# テスト用のtemplates指定
templates = Jinja2Templates(directory="templates")


class MyPostData(BaseModel):
    name: str
    mean: str

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


#いいね全抽出
@app.get('/likes/')
def read_likes(db: Session = Depends(get_db)):
    likes = crud.get_likes(db)

    return likes

#指定ユーザーいいね機能
@app.post("/users/{user_id}/likes")
def create_likes_for_user(
    user_id: int, post_id: int, like: schemas.LikesCreate, db: Session = Depends(get_db)
):
    return crud.create_user_like(db=db, like=like, user_id=user_id, post_id=post_id)

#いいね指定抽出
@app.get("/users/{user_id}/likes")
def read_like(user_id: int, db: Session = Depends(get_db)):
    db_like = crud.get_user_like(db, user_id=user_id)

    if db_like is None:
        db_like = []
    return db_like

#いいね投稿別一覧表示
@app.get("/posts/{post_id}/likes")
def read_post_like(post_id: int, db: Session = Depends(get_db)):
    db_post_like = crud.get_post_like(db, post_id=post_id)
    if db_post_like is None:
        db_post_like = 0
    return db_post_like
    
#コメント機能
@app.post('/users/{user_id}/comments/')
def create_comment_for_user(comment: schemas.CommentsCreate, db: Session = Depends(get_db)):
    return crud.post_comment(db=db, comment=comment)

#コメント
@app.get('/posts/{post_id}/comments/')
def read_comment(post_id: int, db: Session = Depends(get_db)):
    db_comment = crud.get_post_comment(db, post_id=post_id)
    if db_comment is None:
        db_comment = 0
    return db_comment



class CreateLikeinfo(BaseModel):
    postid: int
    user_id: int


class Likeinfo(BaseModel):
    postid: int

class MyLikeinfo(BaseModel):
    user_id: int


#いいね数取得
@app.get('/get_cntlike')
def cnt_getlike(button: Likeinfo ,db: Session = Depends(get_db)):
    postid = button.postid
    # postid=7
    records = crud.get_post_like(db, postid)


    return records




@app.get('/get_mylike')
def get_Mylike(db: Session = Depends(get_db)):
    mylikelist = []
    myyoutubelist = []
    user_id = 1
    useralllike = crud.get_user_like(db, user_id)
    
    
    for idx in range(len(useralllike)):
       mylikelist.append(useralllike[idx]["POST_ID"])


    for i in range(len(mylikelist)):
        userPOST = crud.get_mylikeyoutube(db, mylikelist[i])
        print(i)
        myyoutubelist.append(userPOST) 

   #ROW OBJECTになってしまっているためうごかない 
   #DBから帰ってくるデータの型をmaなどのライブラリで
   #特殊なオブジェクトから配列で帰ってくるように変更するまで保留
    for x in range(len(mylikelist)):
        TrueyoutubeURL =  "https://www.youtube.com/embed/" + myyoutubelist[0][0]["YOUTUBE"]
        # myyoutubelist[0][0]["YOUTUBE"] = TrueyoutubeURL
        myyoutubelist[0][0]["YOUTUBE"] = "11"
    # youtubeURL = myyoutubelist[0][0]["YOUTUBE"]


    return myyoutubelist





#いいね機能
@app.post('/users/{user_id}/likes/')
def create_likes_for_user(button: CreateLikeinfo ,like: schemas.LikesCreate,db: Session = Depends(get_db)):
    user_id= button.user_id
    post_id= button.post_id
    return crud.create_user_like(db=db, like=like, user_id=user_id, post_id=post_id)



if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)