
from sqlalchemy.orm import Session, session #テーブルをつくったらここにモジュール追加
from models.dbSchemas import UsersTable as users 
from models.dbSchemas  import LikesTable as likes
from models.dbSchemas  import CommentsTable as comments #
from models.dbSchemas  import PostTable as posts
from models.dbSchemas  import TestTasksTable as tasks 
import models.schemas as schemas
from sqlalchemy import desc


# 全てのCRUD処理をここに記述。
# CRUD名_テーブル名

# @app.get('/User')
# def get_login_list(db: Session = Depends(get_db)):
#     user = crud.get_login_list(db)
#     for row in user:
#         d = row.__dict__
#     return d['MAIL']

LIST = []


#select * from tasks
def get_tasks(db: Session):
    return  db.query(tasks).all()

def create_task(db: Session, task: schemas.TestTaskCreate):
    db_task = tasks(name=task.name, content=task.content)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)

    return db_task

def get_login_list(db: Session):
    return db.query(users).all()

def get_user_by_email(db: Session, mail: str):
    return db.query(users).filter(users.MAIL == mail).first()

def create_user(db: Session, user: schemas.UsersCreate):
    db_user = users(MAIL=user.mail, PASSWORD=user.password)
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

#動画投稿機能
def post_movie(db: Session, post: schemas.PostsCreate, url: str, userid: int, caption: str, title: str):
    db_post = posts(USER_ID=userid, YOUTUBE=url,
    CAPTION=caption, TITLE=title)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

#いいね全一覧
def get_likes(db: Session):
    getlikes = db.query(likes).all()

    for idx in range(len(getlikes)):
        LIST.append(getlikes[idx].__dict__)

    return LIST

#いいねuser別一覧
def get_user_like(db: Session, user_id: int):
    alluserlike = db.query(likes).filter(likes.USER_ID == user_id).all()
    
    for idx in range(len(alluserlike)):
       LIST.append(alluserlike[idx].__dict__)


    return LIST

#いいね投稿別一覧
def get_post_like(db: Session, postid: int):
    return db.query(likes).filter(likes.POST_ID == postid).count()

# def cnt_get_post_like(db: Session, post_id: int):
#     cnt = get_post_like(db: Session, post_id)
#     return cnt
    
#いいね機能
def create_user_like(db: Session, like:schemas.LikesCreate, user_id: int, post_id: int):
    db_like = likes(USER_ID=user_id, POST_ID=post_id)
    db.add(db_like)
    db.commit()
    return db_like

#コメント機能
def post_comment(db: Session, comment: schemas.CommentsCreate):
    db_comment = comments(POST_ID=comment.post_id, USER_ID=comment.user_id,
    COMMENTS=comment.comments)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

#コメント投稿別一覧
def get_post_comment(db: Session, post_id: int):
    return db.query(comments).filter(comments.POST_ID == post_id).all()

#現在の最新の投稿を取り出す
def get_latest_post(db: Session):
    latest = db.query(posts.ID).order_by(desc(posts.ID)).first()
    return latest


# ログインを試行する
# def try_login(form,db: Session):
    # USER_LOGIN_LIST = get_login_list(db)
#     mail = form.get('mail', '')
#     password = form.get('pw', '')
#     print('入力されたメールアドレス'+ mail)
#     print('入力されたパスワード' + password)
#     userlen = len(USER_LOGIN_LIST)
#     if userlen == 0:
import time
#ログインを試行する
def try_login(form, db: Session):
    USER_LOGIN_LIST = get_login_list(db)

    # データ型をリスト内辞書に変換
    for user in USER_LOGIN_LIST:
        LIST.append(user.__dict__)
    
    mail = form.mail
    password = form.password
    print('入力されたメールアドレス'+ mail)
    print('入力されたパスワード' + password)
    userlen = len(USER_LOGIN_LIST)


    print(userlen)
    if userlen == 0:
        return "wrong username or password"

    time.sleep(0.5)  
    for i in range(userlen):
        print('ユーザーリストのmail: ' + LIST[i]['MAIL'])
        print('ユーザリストのpassword: ' + LIST[i]['PASSWORD'])
        for idx in range(userlen):

            if mail != LIST[i]['MAIL'] and password != LIST[i]['PASSWORD']:
                continue
            elif mail == LIST[i]['MAIL'] and password != LIST[i]['PASSWORD']:
                continue
            elif mail != LIST[i]['MAIL'] and password == LIST[i]['PASSWORD']:
                continue
            else:
                return True
                # result = True
            # if mail == LIST[i]['MAIL'] and password == LIST[i]['PASSWORD']:
            #     result = True
            #     break
            #     # return True
            #     # session['login'] = users
            # else:
            #     result = False
            #     # return "wrong username or password"
        

    



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

    allposts = db.query(posts).all()
    for post in allposts:
        LIST.append(post.__dict__)


    return LIST



# 最新の20件の投稿を表示する 
# select * from POSTS limit 20;
def get_postAthome(db: Session):

    latestposts = db.query(posts).order_by(desc(posts.CREATED_AT)).limit(20).all() 
    for latest in latestposts:
        LIST.append(latest.__dict__)

    
    return LIST

def get_sessioninfo(db: Session):

    sessioninfo = db.query(users.USERSTable.MAIL).all()

    return sessioninfo



def search_userid(db: Session, mail):

    mail = db.query(users.ID).filter(users.MAIL == mail).all()

    return mail




def get_allyoutube(db: Session):

    youtube = db.query(posts).all()
    for ytb in youtube:
        LIST.append(ytb.__dict__)

    return LIST

def get_youtube(db: Session, postid):

    Oneyoutube = db.query(posts).filter(posts.ID == postid).all()
    for ytb in Oneyoutube:
        LIST.append(ytb.__dict__)

    return LIST

def get_latestyoutube(db: Session):
    LIST = []
    youtube = db.query(posts).order_by(desc(posts.CREATED_AT)).limit(20).all() 
    for ytb in youtube:
        LIST.append(ytb.__dict__)

    return LIST

def get_mylikeyoutube(db: Session, post_id):
    LIST = []
    youtube = db.query(posts.USER_ID, posts.CAPTION, posts.TITLE,posts.YOUTUBE).order_by(desc(posts.CREATED_AT)).all() 
    for ytb in youtube:
        LIST.append(ytb.__dict__)

    return LIST

def get_mylikeyoutubeURL(db: Session):
    URLlist = []
    numOfrecords = db.query(posts).query.count()
    for iter in range(numOfrecords):
        url = db.query(users).filter(posts.ID == iter+1).one().toDict()
        url["YOUTUBE"] = "https://www.youtube.com/embed/" + url["YOUTUBE"]
        URLlist.append(url["YOUTUBE"])
        return URLlist

