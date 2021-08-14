
# from app.python.models.schemas import Users
from models.schemas import *
from fastapi import FastAPI, Depends, HTTPException, Request, File, UploadFile
from fastapi.responses import HTMLResponse, ORJSONResponse, RedirectResponse, FileResponse, StreamingResponse
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

from models.fromFrontClasses import LoginUserInfo
import os, re, ast, shutil, cv2, sys, numpy

app=FastAPI()
tasks.Base.metadata.create_all(bind=ENGINE)

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
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# テスト用辞書
test_data = {
    "pachinko": "玉を弾く遊び",
    "slot": "リールを回す遊び",
}

class Data(BaseModel):
    user: str


@app.post("/")
def main(data: Data):
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

@app.get("userloginlist")
def get_user(db: Session = Depends(get_db)):
    USER_LOGIN_LIST = crud.get_userlist(db)
    return USER_LOGIN_LIST


class UserInfo(BaseModel):
    email: str
    password: str

@app.get('/getforsession')
def get_session(db: Session = Depends(get_db)):
    userinfo = crud.get_userforsession(db)
    return userinfo


#ログイン試行
@app.post('/login/')
def login_try(form:UserInfo, db: Session = Depends(get_db)):
    print(form.email, form.password)
    can_login = crud_try_login(form,db)
    if can_login:
        # users = crud.get_userforsession(db)
        session['login'] = users
        return True
    return False
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

#いいね抽出
@app.get('/likes/')
def read_likes(db: Session = Depends(get_db)):
    likes = crud.get_likes(db)
    return likes

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




@app.get("/fileupload/filelist", response_class=ORJSONResponse)
async def get_filelist(request: Request):
    '''docstring
    アップロードされたファイルの一覧を取得する
    '''

    def get_extention(filepath):
        '''docstring
        ファイルパスから拡張子を取得する
        '''

        ex = os.path.sqlitext(filepath)
        return ex[len(ex)-1]

    uploadedpath = "./uploads"
    files = os.listdir(uploadedpath)
    filelist = [{
        "filename":f,
        "filesize": os.path.getsize(os.path.join(uploadedpath, f)),
        "extention": get_extention(f),
    } for f in files if os.path.isfile(os.path.join(uploadedpath, f))]
    return filelist








# @app.post("/fileupload/upload")
# async def fileupload_post(request: Request):
#     '''docstring
#     アップロードされたファイルを保存する
#     '''

#     form = await request.form()
#     uploadedpath = "./uploads"
#     files = os.listdir(uploadedpath)
#     for formdata in form:
#         uploadfile = form[formdata]
#         path = os.path.join("./uploads", uploadfile.filename)
#         fout = open(path, 'wb')
#         while 1:
#             chunk = await uploadfile.read(100000)
#             if not chunk: break
#             fout.write (chunk)
#         fout.close()
    
#     return {"status": "OK"}

@app.post("/fileupload/deletefile")
async def deletefile_post(request: Request):
    '''docstring
    ファイルを削除する  
    '''

    form = await request.form()
    for formdata in form:
        formparams = form[formdata]
        dictparams = ast.literal_eval(formparams)
        os.remove(os.path.join("./uploads", dictparams.get('filename')))
    response = RedirectResponse(url='/fileupload2', status_code=HTTP_302_FOUND)
    return response



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
# 最新の投稿20件を表示する
def get_PostAthome(db: Session = Depends(get_db)):

    Latestposts = crud.get_postAthome(db)

    return Latestposts


# 1件だけ動画をとってくる
@app.get("/get_movie")
def get_filemovie():

    cap = cv2.VideoCapture(FILES_DIR + 'sample_movie.mp4')
    #動画のながさ  
    movie = cap.get(cv2.CAP_PROP_FRAME_COUNT) / cap.get(cv2.CAP_PROP_FPS)

    return movie

# @app.post("/send_movie")
# def gen():
#     cap = cv2.VideoCapture(FILES_DIR + 'sample_movie.mp4')



if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0",port=8000,reload=True)



