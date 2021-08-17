import os, cv2
import time
import pathlib
from fastapi import APIRouter, Depends,Cookie
from pathlib import Path
from models import schemas,crud
from pydantic.main import BaseModel
from sqlalchemy.orm import Session, session
from tempfile import NamedTemporaryFile
from database import get_db
import shutil
router = APIRouter()
#ディレクトリ先の指定
BASE_DIR = os.path.dirname(__file__)
FILES_DIR = BASE_DIR + '/files/'

class PostInfo(BaseModel):
    # thumbnail_id: str
    # user_id: int
    userid: int
    youtube: str
    caption: str
    title: str

#YoutubeでURLにて投稿機能とqrコード作成機能
@router.post('/up/')
def create_youtube(form: PostInfo ,post: schemas.PostsCreate, db: Session = Depends(get_db)):
    youtubeurl = form.youtube
    url = youtubeurl.replace('https://www.youtube.com/watch?v=', '')
   

    # file_name = url + '.png'
    # img = youtubeurl
    # qrimg = qrcode.make(img)


    return crud.post_movie(db=db, post=post, url=url, userid=form.userid, title=form.title, caption=form.caption)
    # return crud.post_movie(db=db, post=post, url=url, userid=form.userid, title=form.title, caption=form.caption), FileResponse(qrimg)

#動画投稿機能
@router.post('/posts/')
def create_post_for_user( form:PostInfo, db: Session = Depends(get_db), post: UploadFile = File(...)):
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
    print(urlyoutube[0])
    for i in range(len(urlyoutube)):
        embed_url = urlyoutube[i]['YOUTUBE']
        movie_id = urlyoutube[i]['ID']
        URLID_LIST.append({"url":"https://www.youtube.com/embed/"+embed_url,"movie_id":movie_id,"youtube_id": "https://img.youtube.com/vi/" + embed_url +"/sddefault.jpg"})
    
    return URLID_LIST



