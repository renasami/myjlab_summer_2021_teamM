import os, cv2

from fastapi.datastructures import UploadFile
import time
import pathlib
from fastapi import APIRouter, Depends,Cookie,File, UploadFile, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
from models import schemas,crud,dbSchemas
from pydantic.main import BaseModel
from sqlalchemy.orm import Session, session
from tempfile import NamedTemporaryFile
from database import get_db
import shutil
router = APIRouter()

templates = Jinja2Templates(directory="./templates")

#ディレクトリ先の指定
BASE_DIR = os.path.dirname(__file__)
FILES_DIR = BASE_DIR + '/files/'
class MyPostData(BaseModel):
    name: str
    mean: str


class PostInfo(BaseModel):
    # thumbnail_id: str
    # user_id: int
    userid: int
    youtube: str
    caption: str
    title: str

@router.post('/up/')
async def create_youtube(USER_ID: int = Form(...), YOUTUBE: str = Form(...), CAPTION: str = Form(...), TITLE: str = Form(...)):
    youtubeurl = YOUTUBE
    url = youtubeurl.replace('https://www.youtube.com/watch?v=', '')
    return {"USER_ID": USER_ID, "YOUTUBE": url, "CAPTION": CAPTION, "TITLE": TITLE}

    # file_name = url + '.png'
    # img = youtubeurl
    # qrimg = qrcode.make(img)


    return crud.post_movie(db=db, post=post, url=url, userid=form.userid, title=form.title, caption=form.caption)
    # return crud.post_movie(db=db, post=post, url=url, userid=form.userid, title=form.title, caption=form.caption), FileResponse(qrimg)

#動画投稿機能
@router.post('/posts/')
def create_post_for_user(form:PostInfo, db: Session = Depends(get_db), post: UploadFile = File(...)):
    print(form)
    crud.post_movie(db, form.title, form.caption, session['login'])
    post_id = db
    try:
        suffix = pathlib(post.filename).suffix
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


#アップロード
@router.post('/upload')
def upload_movie(USER_ID: int = Form(...), YOUTUBE: str = Form(...), CAPTION: str = Form(...), TITLE: str = Form(...), db: Session = Depends(get_db)):
    crud.post_movie(db, YOUTUBE, USER_ID, CAPTION, TITLE)
    return "success"



#動画サムネイル
@router.get('/moviephoto/')
def get_photo():
    file = 'test1.mp4'
    cap = cv2.VideoCapture(file)
    cap.set(cv2.CAP_PROP_POS_MSEC, 1000)
    res, img = cap.read()
    cv2.imwrite('test.png', img)
    

#動画をみせる

@router.get("/allmovie")
# 投稿されている全ての動画の情報をすべて取得 ホームページで使う
def get_Allmovie(db: Session = Depends(get_db)):
    
    allmovie = crud.get_allmovie(db)
    
    return allmovie

@router.get("/movieAthome")
def get_movieathome(db: Session = Depends(get_db)):

    latestmovie = crud.get_movieAthome(db)

    return latestmovie


# 全ての投稿を表示する
@router.get("/allposts")
def get_Allposts(db: Session = Depends(get_db)):

    Allposts = crud.get_allposts(db)
    
    return Allposts

@router.get("/latestposts")
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
@router.get("/get_URL")
def get_url(db: Session = Depends(get_db)):
    time.sleep(0.5)
    URLID_LIST = []
    time.sleep(0.5)
    urlyoutube = crud.get_latestyoutube(db)
    print("=========================")
    print(urlyoutube)
    for i in range(len(urlyoutube)):
        embed_url = urlyoutube[i]['YOUTUBE']
        movie_id = urlyoutube[i]['ID']
        URLID_LIST.append({"url":"https://www.youtube.com/embed/"+embed_url,"movie_id":movie_id,"youtube_id": "https://img.youtube.com/vi/" + embed_url +"/sddefault.jpg"})
    
    return URLID_LIST



templates = Jinja2Templates(directory="./templates")


# formのページ用意
@router.get("/{id}", response_class=HTMLResponse)
async def post_HTML(request: Request, id: str):
    return templates.TemplateResponse("post.html", {"request": request, "id": id})