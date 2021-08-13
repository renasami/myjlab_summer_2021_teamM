from sqlalchemy.orm import Session
from . import tasks, schemas, comments, likes, movies, musics, posts, users #テーブルをつくったらここにモジュール追加
import cv2



# 全てのCRUD処理をここに記述。
# CRUD名_テーブル名


def get_tasks(db: Session):
    return db.query(tasks.TestTasksTable).all()

def create_task(db: Session, task: schemas.TestTaskCreate):
    db_task = tasks.TestTasksTable(name=task.name, content=task.content)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)

    return db_task






# 動画のpathをDBに保存する
def post_movie(db: Session, movie: schemas.MoviesSend):
    db_movie = movies.MOVIESTable(MOVIES=movie.moviepath, POST_ID=movie.post_id)
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)

    return db_movie
