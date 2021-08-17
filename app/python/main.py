
# from app.python.models.schemas import Users
from tempfile import NamedTemporaryFile
from typing import Optional
from starlette.websockets import WebSocket
from starlette import status
from models.schemas import *
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
from pathlib import Path
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

# 動画の保存ディレクトリ先の指定
BASE_DIR = os.path.dirname(__file__)
FILES_DIR = BASE_DIR + '/files/'



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




@app.get("/userloginlist")
def get_user(db: Session = Depends(get_db)):
    USER_LOGIN_LIST = crud.get_login_list(db)
    return USER_LOGIN_LIST



#ユーザー一覧
@app.get('/User')
def get_login_list(db: Session = Depends(get_db)):
    user = crud.get_login_list(db)
    for row in user:
        d = row.__dict__
    return d['MAIL']


class UserInfo(BaseModel):
    mail: str
    password: str


    
@app.post('/login/')
def login_try(form:UserInfo, user_id :Optional[int] = Cookie(None),db: Session = Depends(get_db)):

    print(form)
    can_login = crud.try_login(form,db)

    if can_login:
        users = crud.search_userid(db, form.mail)
        print(users)
        # print(Cookie[0])
        # session['login'] = form.mail
        return True, {"user_id" : users[0][0]}
    return False


    
  
#新規会員登録
@app.post('/register/')
def create_user(user: schemas.UsersCreate, db: Session = Depends(get_db)):
    db_user  = crud.get_user_by_email(db, mail=user.mail)
    if db_user != None:
        raise HTTPException(status_code=400, detail="このメールアドレスは会員登録が完了しています")
    return crud.create_user(db=db, user=user)

class PostInfo(BaseModel):
    # thumbnail_id: str
    # user_id: int
    userid: int
    youtube: str
    caption: str
    title: str

#YoutubeでURLにて投稿機能とqrコード作成機能
@app.post('/up/')
def create_youtube(form: PostInfo ,post: schemas.PostsCreate, db: Session = Depends(get_db)):
    youtubeurl = form.youtube
    url = youtubeurl.replace('https://www.youtube.com/watch?v=', '')
   

    # file_name = url + '.png'
    # img = youtubeurl
    # qrimg = qrcode.make(img)


    return crud.post_movie(db=db, post=post, url=url, userid=form.userid, title=form.title, caption=form.caption)
    # return crud.post_movie(db=db, post=post, url=url, userid=form.userid, title=form.title, caption=form.caption), FileResponse(qrimg)

#動画投稿機能
@app.post('/posts/')
def create_post_for_user( form:PostInfo, db: Session = Depends(get_db), post: UploadFile = File(...)):
    crud.post_movie(db, form.title, form.caption, session['login'])
    post_id = db
    try:
        suffix = Path(post.filename).suffix
        with NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            shutil.copyfileobj(post.file, tmp)
            tmp_path = Path(tmp.name)
            namefile = crud.get_latest_post(db) + ".mp4"
            renamedfile = os.rename(suffix, namefile)

    finally:
        post.file.close()
    return tmp_path
    # test = open(post)
    # print(test)
    #return crud.post_movie(db=db, post=post)

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


#動画サムネイル
@app.get('/moviephoto/')
def get_photo():
    file = 'test1.mp4'
    cap = cv2.VideoCapture(file)
    cap.set(cv2.CAP_PROP_POS_MSEC, 1000)
    res, img = cap.read()
    cv2.imwrite('test.png', img)
    

#動画をみせる

@app.get("/allmovie")
# 投稿されている全ての動画の情報をすべて取得 ホームページで使う
def get_Allmovie(db: Session = Depends(get_db)):
    
    allmovie = crud.get_allmovie(db)
    
    return allmovie

@app.get("/movieAthome")
def get_movieathome(db: Session = Depends(get_db)):

    latestmovie = crud.get_movieAthome(db)

    return latestmovie






# 全ての投稿を表示する
@app.get("/allposts")
def get_Allposts(db: Session = Depends(get_db)):

    Allposts = crud.get_allposts(db)
    
    return Allposts


@app.get("/latestposts")
# 最新の20件投稿を表示する
def get_PostAthome(db: Session = Depends(get_db)):

    Latestposts = crud.get_postAthome(db)
    # ret_arr = []
    # for n in range(len(Latestposts)):
    #     ret_arr.append(Latestposts[n].__dict__)
    # print(type(ret_arr[0]))
    # print(type(ret_arr))
    return Latestposts


#youtube URLの取得(最新20件)
@app.get("/get_URL")
def get_url(db: Session = Depends(get_db)):
    time.sleep(0.5)
    URLID_LIST = []
    time.sleep(0.5)
    urlyoutube = crud.get_latestyoutube(db)
    print("=========================")
    print(urlyoutube[0])
    for i in range(len(urlyoutube)):
        embed_url = urlyoutube[i]['YOUTUBE']
        movie_id = urlyoutube[i]['ID']
        URLID_LIST.append({"url":"https://www.youtube.com/embed/"+embed_url,"movie_id":movie_id,"youtube_id": "https://img.youtube.com/vi/" + embed_url +"/sddefault.jpg"})
    
    return URLID_LIST



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