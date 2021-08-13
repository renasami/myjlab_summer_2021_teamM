from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from models import crud, tasks, schemas, comments, likes, movies, musics, posts, users   #テーブル作成したら随時追加
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






































@app.get("/movie")
# 動画ファイルを受け取る
def get_movie():

    #動画ファイルを受け取る処理書く、でもわからん。

    # 受け取ったファイル形式をチェック、mp4ファイルだけを許可
    if not re.search(r'\.(mp4)$', upfile.filename):
        print('mp4ファイルではない:', upfile.filename)
        return 0



# # 動画ファイルをmoviesテーブルのidと同じ数字にリネームする
# def rename_movie():
    
#     return



# 動画ファイルをfilesディレクトリに保存する
def save_movie(user_id, upfile, post_id):

    frame_rate = 24.0 #フレームレート
    size = (640, 480) #動画の画面サイズ

    fmt = cv2.VideoWrite_fourcc('m', 'p', '4', 'v') #ファイル形式指定(ここではmp4)

    #指定したディレクトリ、名前、フレームレート、ファイル形式、動画の画面サイズで動画を保存 
    writer = cv2.VideoWriter('./files/' + rename_movie(upfile) + '.mp4', fmt, frame_rate, size) 

    ret, frame = video.read()
    writer.write(frame) #画像を1フレーム分として書き込み

    writer.release() #ファイルを閉じる

     
    # # ファイル情報を保存
    # file_id = exec('''
    #     INSERT INTO MOVIES (USER_ID, MOVIENAME, POST_ID)
    #     VALUES(?,?,?)''',
    #     user_id, moviename, post_id
    # )

    crud.post_movie(db=db, movie=movie)


#動画ファイルの保存先pathを取得
def get_moviepath():
    return FILES_DIR + '/' + str(file_id) + ptype + '.mp4'


@app.post("/movie")
def send_movie(movie: schemas.MoviesSend, db: Session = Depends(get_db)):
    
    movie = crud.post_movie(db=db, movie=movie)



    return movie

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


    