from sqlalchemy.orm import Session
from . import tasks, schemas, comments, likes, movies, musics, posts, users #テーブルをつくったらここにモジュール追加
import cv2



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


# 動画のpathをDBからとってくる
def get_postmovie(db: Session):

    return db.query(movies.MOVIESTable).all()

def get_mylikemovie(db: Session):
    


    return db.query(movies.MOVIESTable).filter(movies.MOVIESTable.USER_ID == ).all()