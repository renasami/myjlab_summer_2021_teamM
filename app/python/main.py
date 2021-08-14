
# from app.python.models.schemas import Users

from models.schemas import *

from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from models import crud, tasks, schemas, comments, likes, posts, users   #テーブル作成したら随時追加
from models.database import session, ENGINE
import os, re

app=FastAPI()
tasks.Base.metadata.create_all(bind=ENGINE)


# 動画の保存ディレクトリ先の指定
BASE_DIR = os.path.dirname(__file__)
FILES_DIR = BASE_DIR + '/files'




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
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# テスト用辞書
test_data = {
    "pachinko": "玉を弾く遊び",
    "slot": "リールを回す遊び",
}

@app.get("/")
async def index():
    return {"message": "hello world"}


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

@app.get("userloginlist")
def get_user(db: Session = Depends(get_db)):
    USER_LOGIN_LIST = crud.get_userlist(db)
    return USER_LOGIN_LIST

#ログイン試行
@app.post('/login')
def login_try(db: Session = Depends(get_db)):
    can_login = crud.try_login(db)
    ok = crud.try_login(request.form, db)

#新規会員登録
@app.post('/users/')
def create_user(user: schemas.UsersCreate, db: Session = Depends(get_db)):
    db_user  = crud.get_user_by_email(db, mail=user.mail)
    if db_user:
        raise HTTPException(status_code=400, detail="このメールアドレスは会員登録が完了しています")
    return crud.create_user(db=db, user=user)

#動画投稿機能
@app.post('/posts/')
def create_post_for_user(post: schemas.PostsCreate, db: Session = Depends(get_db)):
    return crud.post_movie(db=db, post=post)

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

# @app.get("/movie")
# # 動画ファイルを受け取る upfileと仮定
# def get_movie():

#     #動画ファイルを受け取る処理書く、でもわからん。
    # upfile = 
#     # 受け取ったファイル形式をチェック、mp4ファイルだけを許可
#     if not re.search(r'\.(mp4)$', upfile.filename):
#         print('mp4ファイルではない:', upfile.filename)
#         return 0



# # 動画ファイルをmoviesテーブルのidと同じ数字にリネームする
# def rename_movie():

#     namefile = ムービーid

#     renamedfile = os.rename(upfile, namefile)

#     return renamedfile


# @app.get("/save_movie")
# # 動画ファイルをfilesディレクトリに保存する
# def save_movie(user_id, renamedfile, post_id):

#     frame_rate = 24.0 #フレームレート
#     size = (640, 480) #動画の画面サイズ

#     fmt = cv2.VideoWrite_fourcc('m', 'p', '4', 'v') #ファイル形式指定(ここではmp4)

#     #指定したディレクトリ、名前、フレームレート、ファイル形式、動画の画面サイズで動画を保存 
#     writer = cv2.VideoWriter('./files/' + renamedfile + '.mp4', fmt, frame_rate, size) 

#     ret, frame = video.read()
#     writer.write(frame) #画像を1フレーム分として書き込み

#     writer.release() #ファイルを閉じる

@app.post("/save_movie_info")
def save_file_info(movie: schemas.MoviesSend, db: Session = Depends(get_db)):
    # # 動画ファイル情報を保存
    # file_id = exec('''
    #     INSERT INTO MOVIES (USER_ID, MOVIE, POST_ID)
    #     VALUES(?,?,?)''',
    #     user_id, movie, post_id
    # )

    fileinfo = crud.post_movie(db=db, movie=movie)

    return fileinfo



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

    return Latestposts

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0",port=8000,reload=True)



