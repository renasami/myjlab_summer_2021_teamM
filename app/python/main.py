# from app.python.models.schemas import Users
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from models import crud, tasks, schemas
from models.database import session, ENGINE



app=FastAPI()
tasks.Base.metadata.create_all(bind=ENGINE)
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

    if not ok: return print('ログイン失敗')

#新規登録
@app.post('/register/try')
def register_try():
    res = {}
    res['mail'] = request.form.get('mail')
    res['pw'] = request.form.get('pw')

    exec('''
    INSERT INTO USERS (MAIL, PASSWORD)
    VALUES(?, ?)''',
    res['mail'], res['pw'])



# ログアウト
@app.post('/logout')
def logout():
    crud.try_logout()
    return print('ログアウトしました')

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0",port=8000,reload=True)



