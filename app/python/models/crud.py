
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


LIST = []


#select * from tasks tasksテーブルの全件抽出
def get_tasks(db: Session):
    return  db.query(tasks).all()

#insert into tasks (name, content) values (name, content);
def create_task(db: Session, task: schemas.TestTaskCreate):
    db_task = tasks(name=task.name, content=task.content)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)

    return db_task

# Usersテーブルの全件抽出 DBに登録されているすべてのユーザ情報取得　開発を楽にするためのもの
def get_login_list(db: Session):
    return db.query(users).all()

# メールアドレスを指定してユーザ情報を取得 開発を楽にするためのもの
def get_user_by_email(db: Session, mail: str):
    return db.query(users).filter(users.MAIL == mail).first()

# ユーザ登録機能　開発者を楽にするためのもの
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

#動画投稿機能 開発を楽にするためのもの
def post_movie(db: Session, post: schemas.PostsCreate, url: str, userid: int, caption: str, title: str):
    db_post = posts(USER_ID=userid, YOUTUBE=url,
    CAPTION=caption, TITLE=title)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

#likesテーブルの全件抽出　開発を楽にするためのもの
def get_likes(db: Session):
    getlikes = db.query(likes).all()

    for idx in range(len(getlikes)):
        LIST.append(getlikes[idx].__dict__)

    return LIST

#ユーザIDを指定してそのユーザのいいねした情報をlikesテーブルから取得。のちにユーザごとのいいねした動画表示機能に合わせて使う。
def get_user_like(db: Session, user_id: int):
    alluserlike = db.query(likes).filter(likes.USER_ID == user_id).all()
    
    for idx in range(len(alluserlike)):
       LIST.append(alluserlike[idx].__dict__)


    return LIST

# 投稿を指定していいね数取得 いいね数表示機能のときに使う
def get_post_like(db: Session, postid: int):
    return db.query(likes).filter(likes.POST_ID == postid).count()

    
# 投稿にいいねをする機能
def create_user_like(db: Session, like:schemas.LikesCreate, user_id: int, post_id: int):
    db_like = likes(USER_ID=user_id, POST_ID=post_id)
    db.add(db_like)
    db.commit()
    return db_like

# 投稿にコメントをする機能
def post_comment(db: Session, comment: schemas.CommentsCreate):
    db_comment = comments(POST_ID=comment.post_id, USER_ID=comment.user_id,
    COMMENTS=comment.comments)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

# コメント表示機能 指定した投稿のコメントを全件取得
def get_post_comment(db: Session, post_id: int):
    return db.query(comments).filter(comments.POST_ID == post_id).all()

#現在の最新の投稿を取り出す サンプルコード
def get_latest_post(db: Session):
    latest = db.query(posts.ID).order_by(desc(posts.ID)).first()
    return latest


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





#全ての投稿の情報を表示する 辞書化して返している
# select * from POSTS 
def get_allposts(db: Session):

    allposts = db.query(posts).all()
    for post in allposts:
        LIST.append(post.__dict__)


    return LIST



# 最新の20件の投稿を表示する 辞書化して返している
# select * from POSTS limit 20;
def get_postAthome(db: Session):

    latestposts = db.query(posts).order_by(desc(posts.CREATED_AT)).limit(20).all() 
    for latest in latestposts:
        LIST.append(latest.__dict__)

    
    return LIST



# メールアドレスを指定してユーザidを取得
def search_userid(db: Session, mail):

    mail = db.query(users.ID).filter(users.MAIL == mail).all()

    return mail



# 投稿テーブルからの全件抽出　辞書化して返している
def get_allyoutube(db: Session):

    youtube = db.query(posts).all()
    for ytb in youtube:
        LIST.append(ytb.__dict__)

    return LIST

# 指定した投稿の情報を取得 辞書化して返している
def get_youtube(db: Session, postid):

    Oneyoutube = db.query(posts).filter(posts.ID == postid).all()
    for ytb in Oneyoutube:
        LIST.append(ytb.__dict__)

    return LIST

# 最新20件の投稿の情報を取得 辞書化して返している
def get_latestyoutube(db: Session):
    youtube = db.query(posts).order_by(desc(posts.CREATED_AT)).limit(20).all() 
    for ytb in youtube:
        LIST.append(ytb.__dict__)

    return LIST


# 最新順にユーザid, キャプション,タイトル,ユーチューブの動画固有idを取得 辞書化して返している
def get_mylikeyoutube(db: Session, post_id):
    LIST = []
    youtube = db.query(posts.USER_ID, posts.CAPTION, posts.TITLE,posts.YOUTUBE).order_by(desc(posts.CREATED_AT)).all() 
    for ytb in youtube:
        LIST.append(ytb.__dict__)

    return LIST

# 動画固有idをyoutubeの埋め込みidに変換する関数
def get_mylikeyoutubeURL(db: Session):
    URLlist = []
    numOfrecords = db.query(posts).query.count()
    for iter in range(numOfrecords):
        url = db.query(users).filter(posts.ID == iter+1).one().toDict()
        url["YOUTUBE"] = "https://www.youtube.com/embed/" + url["YOUTUBE"]
        URLlist.append(url["YOUTUBE"])
        return URLlist

