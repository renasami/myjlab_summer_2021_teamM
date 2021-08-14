
from sqlalchemy.orm import Session, session
from . import tasks, schemas, comments, likes, posts, users #テーブルをつくったらここにモジュール追加
import cv2
from sqlalchemy import desc


# 全てのCRUD処理をここに記述。
# CRUD名_テーブル名


#select * from tasks
def get_tasks(db: Session):
    return db.query(tasks.TestTasksTable).all()

def create_task(db: Session, task: schemas.TestTaskCreate):
    db_task = tasks.TestTasksTable(name=task.name, content=task.content)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)

    return db_task


def get_login_list(db: Session):
    return db.query(users.USERSTable).all()


def get_user_by_email(db: Session, mail: str):
    return db.query(users.USERSTable).filter(users.USERSTable.MAIL == mail).first()


def create_user(db: Session, user: schemas.UsersCreate):
    db_user = users.USERSTable(NAME=user.name, MAIL=user.mail, PASSWORD=user.password, PASSWORD_CONFIRMATION=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

#ログアウト
def try_logout():
    session.pop('login', None)

# ログインしているかの確認 --- (*2)
def is_login():
    return 'login' in session

# ログインを試行する
# def try_login(form,db: Session):
#     USER_LOGIN_LIST = get_login_list(db)
#     mail = form.get('mail', '')
#     password = form.get('pw', '')
#     print('入力されたメールアドレス'+ mail)
#     print('入力されたパスワード' + password)
#     userlen = len(USER_LOGIN_LIST)
#     if userlen == 0:
    
#     for i in range(userlen):
#         print('ユーザーリストのmail' + USER_LOGIN_LIST[i]['MAIL'])
#         print('ユーザリストのpassword' +USER_LOGIN_LIST[i]['PASSWORD'])
#         if mail != USER_LOGIN_LIST[i]['MAIL'] and password != USER_LOGIN_LIST[i]['PASSWORD']:
#             print('存在しません。')

#         elif mail == USER_LOGIN_LIST[i]['MAIL'] and password != USER_LOGIN_LIST[i]['PASSWORD']:
#             print('入力したパスワードが間違っています。')

#         elif mail != USER_LOGIN_LIST[i]['MAIL'] and password == USER_LOGIN_LIST[i]['PASSWORD']:
#             print('入力したメールアドレスが間違っています。')
#         else:
#             session['login'] = users
#             return True



# def register_try():
#     res = {}
#     res['mail'] = request.form.get('mail')
#     res['pw'] = request.form.get('pw')

#     exec('''
#     INSERT INTO USERS (MAIL, PASSWORD)
#     VALUES(?, ?)''',
#     res['mail'], res['pw'])


# @app.route('/logout')
# def logout():
#     user.try_logout()
#     return msg('ログアウトしました')





#全ての投稿の情報を表示する
# select * from POSTS 
def get_allposts(db: Session):

    allposts = db.query(posts.POSTSTable).all()

    return allposts



# 最新の20件の投稿を表示する 
# select * from POSTS limit 20;
def get_postAthome(db: Session):

    latestposts = db.query(posts.POSTSTable).order_by(desc(posts.POSTSTable.CREATED_AT)).limit(20).all() 

    
    return latestposts