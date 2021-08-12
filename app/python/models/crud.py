from sqlalchemy.orm import Session
from . import tasks, schemas #テーブルをつくったらここにモジュール追加

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

