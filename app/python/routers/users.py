from typing import Optional
from fastapi.exceptions import HTTPException
from pydantic.main import BaseModel
from models import crud,schemas
from fastapi import APIRouter, Depends,Cookie
from sqlalchemy.orm import Session
from database import get_db
import tracemalloc


router = APIRouter()
class UserInfo(BaseModel):
    mail: str
    password: str

@router.get("/")
def user_test():
    return "Hello, user api!"

@router.post("/")
def user_post_test(test:UserInfo):
    print(test)
    resp = "mail: " + test.mail + " pas: " + test.password + " is successfuly post"
    return resp

#ユーザ-一覧
@router.get('/user')
def get_login_list(db: Session = Depends(get_db)):
    tracemalloc.start()
    user = crud.get_login_list(db)
    for row in user:
        yield row.__dict__
        

@router.get("/loginlist")
def get_user(db: Session = Depends(get_db)):
    USER_LOGIN_LIST = crud.get_login_list(db)
    return USER_LOGIN_LIST 

@router.post("/login")
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
@router.post('/register/')
def create_user(user: schemas.UsersCreate, db: Session = Depends(get_db)):
    print(user)
    # db_user  = crud.get_user_by_email(db, mail=user.mail)
    # if db_user != None:
    #     raise HTTPException(status_code=400, detail="このメールアドレスは会員登録が完了しています")
    return crud.create_user(db=db, user=user)



#そいえばログアウト処理バックエンドにないね