
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
from sqlalchemy.orm import Session
from models import crud, tasks, schemas, comments, likes, posts, users   #テーブル作成したら随時追加
from models.crud import try_login as crud_try_login
from models.database import session, ENGINE
from pathlib import Path
from models.fromFrontClasses import LoginUserInfo
import os, re, ast, cv2, shutil, qrcode
from typing import Optional
from fastapi.security import APIKeyCookie


# from starlette.middleware.sessions import SessionMiddleware
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
# import auth

app=FastAPI()

# app.include_router(auth.router, prefix="/auth")
tasks.Base.metadata.create_all(bind=ENGINE)
clients = {}

# テスト用のtemplates指定
templates = Jinja2Templates(directory="templates")

# 動画の保存ディレクトリ先の指定
BASE_DIR = os.path.dirname(__file__)
FILES_DIR = BASE_DIR + '/files/'



def get_db():
    try:
        db = session()
        yield db
    finally:
        db.close()
        print('closed database')

class MyPostData(BaseModel):
    name: str
    mean: str

origins = [
    "http://localhost:8080",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins= ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# テスト用辞書
test_data = {
    "pachinko": "玉を弾く遊び",
    "slot": "リールを回す遊び",
}

@app.post("/")
def main(data):
    print(data)
    return data

@app.get("/data/")
def read_data(key: str):
    return test_data[key]

@app.post("/data/")
def update_data(post_data: MyPostData):
    test_data[post_data.name] = post_data.mean
    return {"message": "post success!!"}


@app.get("/test_task")
def get_task(db: Session = Depends(get_db)):
    tasks = crud.get_tasks(db)
    return tasks

@app.post("/test_task")
def create_task(task: schemas.TestTaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db=db, task=task)

@app.get("/userloginlist")
def get_user(db: Session = Depends(get_db)):
    USER_LOGIN_LIST = crud.get_login_list(db)
    return USER_LOGIN_LIST


# @app.get("/searchforsession")
# def search_session(db: Session = Depends(get_db)):
#     mail = "kaisei@gmail.com"
#     searchinfo = crud.search_mail(db, mail)

#     return searchinfo

# @app.get("/user")
# def get_index(username: str = Depends(auth.verify_token)):
#     print("get_index: %s" % username)
#     return {"username": username}

#ユーザー一覧
@app.get('/User')
def get_login_list(db: Session = Depends(get_db)):
    user = crud.get_login_list(db)
    for row in user:
        d = row.__dict__
    return d['MAIL']

#ログイン試行
# @app.post('/login')
# def login_try(db: Session = Depends(get_db)):
#     can_login = crud.try_login(db)
#     ok = crud.try_login(request.form, db)


#ログイン試行

# @app.get('/users')
# def check(db: Session = Depends(get_db)):
#     test = crud.try_login(db)

#     return test
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
        return True, {"user_id" : users}
    return False


    
  
#新規会員登録
@app.post('/register/')
def create_user(user: schemas.UsersCreate, db: Session = Depends(get_db)):
    db_user  = crud.get_user_by_email(db, mail=user.mail)
    if db_user != None:
        raise HTTPException(status_code=400, detail="このメールアドレスは会員登録が完了しています")
    return crud.create_user(db=db, user=user)

# @app.get('/User')
# def get_login_list(db: Session = Depends(get_db)):
#     user = crud.get_login_list(db)
#     for row in user:
#         d = row.__dict__
#     typed = type(d)
#     return d['MAIL'], typed

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
   

    file_name = url + '.png'
    img = youtubeurl
    qrimg = qrcode.make(img)


    return crud.post_movie(db=db, post=post, url=url, userid=form.userid, title=form.title, caption=form.caption), FileResponse(qrimg)

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
        db_like = 0
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
    
# @app.get("/movie")
# # 動画ファイルを受け取る upfileと仮定
# def get_movie():

#     #動画ファイルを受け取る処理書く、でもわからん。
    # upfile = 
#     # 受け取ったファイル形式をチェック、mp4ファイルだけを許可
#     if not re.search(r'\.(mp4)$', upfile.filename):
#         print('mp4ファイルではない:', upfile.filename)
#         return 0


# @app.get('/movie')
# # 動画ファイルをmoviesテーブルのidと同じ数字にリネームする
# def rename_movie():

#     namefile = ムービーid

#     renamedfile = os.rename(upfile, namefile)

#     return renamedfile



# @app.get("/fileupload")
# async def fileupload(request: Request):
#     '''docstring
#     ファイルアップロード(初期表示)
#     '''
#     html_content = """
#     <html>
#         <head>
#             <title>Some HTML in here</title>
#         </head>
#         <body>
#             <h1>Look ma! HTML!</h1>
#             <form method=post action="/fileupload/upload">
#                 <p>アップロードするファイルを選択してください.</p>
#                 <p><input type="file"></p>
#                 <input type="submit" value="アップロード">
#             <form>
#         </body>
#     </html
#     """
#     return HTMLResponse(content=html_content, status_code=200)

# @app.post("/fileupload/upload")
# async def image(file: UploadFile = File(...)):
#     global upload_folder
#     print("1")

#     file_object = file.file

#     print("2")

#     upload_folder = open(os.path.join(upload_folder, file.filename), 'wb+')

#     print("3")
#     shutil.copyfileobj(file_object, upload_folder)

#     print("4")

#     upload_folder.close()

#     print("5")

#     return {'filename': file.filename}











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



# # 自分がいいねした動画のみをすべて取得
# def get_Mylikemovie(db: Session = Depends(get_db)):
    
#     mylike = crud.get_mylikemovie(db) 

#     return mylike


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

# @app.get("/get_url")
# def get_youtube(db: Session = Depends(get_db)):

#     urlyoutube = crud.get_allyoutube(db)
#     url = urlyoutube.__str__
    
#     return type(url)

# @app.get("/get_oneURL")
# def get_Oneyoutube(db: Session = Depends(get_db)):

#     postid = 7
#     oneurl = crud.get_youtube(db, postid)
#     embedURL = "https://www.youtube.com/embed/" + oneurl[0]["YOUTUBE"]

#     return embedURL


#youtube URLの取得(最新20件)
@app.get("/get_URL")
def get_url(db: Session = Depends(get_db)):
    LIST = []
    urlyoutube = crud.get_latestyoutube(db)
    for i in range(len(urlyoutube)):
        embedURL = "https://www.youtube.com/embed/" + urlyoutube[i]['YOUTUBE']
        LIST.append(embedURL)
    
    return LIST

# @app.get("/qr")
# def make_qr():
#     file_name = FILES_DIR +'test.png'
#     qr = "https://www.youtube.com/watch?v=Fa1UPDtZBYY"
#     img = qrcode.make(qr)
#     img.save(file_name)

#     return


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


#自分のいいねした動画取得 未完、 youtubeURLを
@app.get('/get_mylike')
def get_mylike(button: MyLikeinfo,  db: Session = Depends(get_db)):
    user_id = button.user_id
    return crud.get_user_like(db, user_id)


# @app.get('/get_mylike')
# def get_mylike(db: Session = Depends(get_db)):
#     # user_id = button.user_id
#     user_id = 1
#     userlike = crud.get_user_like(db, user_id)
    
    # return

#いいね機能
@app.post('/users/{user_id}/likes/')
def create_likes_for_user(button: CreateLikeinfo ,like: schemas.LikesCreate,db: Session = Depends(get_db)):
    user_id= button.user_id
    post_id= button.post_id
    return crud.create_user_like(db=db, like=like, user_id=user_id, post_id=post_id)

# いいね機能テストコード
# @app.post('/users/{user_id}/likes/')
# def create_likes_for_user(like: schemas.LikesCreate,db: Session = Depends(get_db)):
#     user_id=1
#     post_id=1
#     return crud.create_user_like(db=db, like=like, user_id=user_id, post_id=post_id)



# @app.post('/post_like')
# def post_like(button: CreateLikeinfo, likes=schemas.LikesCreate,db: Session = Depends(get_db)):
#     user_id = button.user_id
#     postid = button.postid

#     return crud.create_user_like(db=db, user_id=user_id, likes=likes, postid=postid)


# @app.websocket("/ws")
# async def websocket_endpoint(ws: WebSocket):
#     await ws.accept
#     #クライアントを識別するためのIDを取得
#     key = ws.headers.get('sec-websocket-key')
#     clients[key] = ws
#     try:
#         while True:
#             # クライアントからメッセージを受信, 
#             # data = await ws.receive_text()
#             receivelike = await crud.create_user_like(db=db)

#             # 接続中のクライアントそれぞれにメッセージを送信(ブロードキャスト)
#             for client in clients.values():
#                 await cnt_getlike()
#     except:
#         await ws.close()
#         #接続切れた場合、当該クライアントを削除する
#         del clients[key]







if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)