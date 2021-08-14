
# from app.python.models.schemas import Users
from tempfile import NamedTemporaryFile
from typing import Optional

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
import os, re, ast, cv2, shutil
from typing import Optional
from fastapi.security import APIKeyCookie


# from starlette.middleware.sessions import SessionMiddleware
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
# import auth

app=FastAPI()

# app.include_router(auth.router, prefix="/auth")
tasks.Base.metadata.create_all(bind=ENGINE)


# テスト用のtemplates指定
templates = Jinja2Templates(directory="templates")

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

#YoutubeでURLにて投稿機能
@app.post('/up/')
def create_youtube(form: PostInfo ,post: schemas.PostsCreate, db: Session = Depends(get_db)):
    youtubeurl = form.youtube
    url = youtubeurl.replace('https://www.youtube.com/watch?v=', '')
    return crud.post_movie(db=db, post=post, url=url, userid=form.userid, title=form.title, caption=form.caption)

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


if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0",port=8000,reload=True)



