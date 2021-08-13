from sqlalchemy.orm import Session
from . import tasks, schemas, comments, likes, movies, musics, posts, users #テーブルをつくったらここにモジュール追加
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


#select * from USERS
def get_userlist(db: Session):

    return db.query(users.USERSTable).all()


# 動画のpathをDBに保存する
def post_movie(db: Session, movie: schemas.MoviesSend):
    db_movie = movies.MOVIESTable(MOVIE=movie.moviepath, POST_ID=movie.post_id, USER_ID=movie.user_id)
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)

    return db_movie





# 全ての動画の情報をDBからとってくる
# select * from MOVIES;
def get_allmovie(db: Session):
    return db.query(movies.MOVIESTable).all()



#最新の動画20件を抽出
# select * from MOVIE order by desc limit 20;
def get_movieAthome(db: Session):
    
    indexpage = db.query(movies.MOVIESTable).order_by(desc(movies.MOVIESTable.CREATED_AT)).limit(20).all()

    # indexpage = db.query(movies.MOVIESTable).order_by(desc(movies.MOVIESTable.created_at)).all()

    # indexpage = db.query(movies.MOVIESTable).limit(20).all()


    return indexpage 
    


# def get_mylikemovie(db: Session):



#     return db.query(movies.MOVIESTable).filter(movies.MOVIESTable.USER_ID == ).all()