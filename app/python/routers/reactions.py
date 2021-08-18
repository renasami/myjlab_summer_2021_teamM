from typing import Optional
from fastapi.exceptions import HTTPException
from pydantic.main import BaseModel
from models import crud,schemas
from fastapi import APIRouter, Depends,Cookie
from sqlalchemy.orm import Session
from database import get_db

router = APIRouter()

@router.get('/likes/')
def read_likes(db: Session = Depends(get_db)):
    likes = crud.get_likes(db)

    return likes

#指定ユーザーいいね機能
@router.post("/users/{user_id}/likes")
def create_likes_for_user(
    user_id: int, post_id: int, like: schemas.LikesCreate, db: Session = Depends(get_db)
):
    return crud.create_user_like(db=db, like=like, user_id=user_id, post_id=post_id)

#いいね指定抽出
@router.get("/users/{user_id}/likes")
def read_like(user_id: int, db: Session = Depends(get_db)):
    db_like = crud.get_user_like(db, user_id=user_id)

    if db_like is None:
        db_like = []
    return db_like

#いいね投稿別一覧表示
@router.get("/posts/{post_id}/likes")
def read_post_like(post_id: int, db: Session = Depends(get_db)):
    db_post_like = crud.get_post_like(db, post_id=post_id)
    if db_post_like is None:
        db_post_like = 0
    return db_post_like
    
#コメント機能
@router.post('/users/{user_id}/comments/')
def create_comment_for_user(comment: schemas.CommentsCreate, db: Session = Depends(get_db)):
    return crud.post_comment(db=db, comment=comment)

#コメント
@router.get('/posts/{post_id}/comments/')
def read_comment(post_id: int, db: Session = Depends(get_db)):
    db_comment = crud.get_post_comment(db, post_id=post_id)
    if db_comment is None:
        db_comment = 0
    return db_comment


#このレベルだとclass要らなくねえかw
class MyLikeinfo(BaseModel):
    user_id: int
class Likeinfo(BaseModel):
    postid: int

#いいね数取得
@router.get('/get_cntlike')
def cnt_getlike(button: Likeinfo ,db: Session = Depends(get_db)):
    postid = button.postid
    # postid=7
    records = crud.get_post_like(db, postid)


    return records

@router.get('/get_mylike')
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




class CreateLikeinfo(BaseModel):
    postid: int
    user_id: int
#いいね機能
@router.post('/users/{user_id}/likes/')
def create_likes_for_user(button: CreateLikeinfo ,like: schemas.LikesCreate,db: Session = Depends(get_db)):
    user_id= button.user_id
    post_id= button.post_id
    return crud.create_user_like(db=db, like=like, user_id=user_id, post_id=post_id)

