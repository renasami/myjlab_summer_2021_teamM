# from app.python.models import name_age_list
from sqlalchemy.orm import Session
from . import tasks, schemas, name_age_list #テーブルをつくったらここにモジュール追加

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

def get_nameagelist(db: Session):
    return db.query(name_age_list.NameAgeListTable).all()

def create_peter(db: Session, nameagelist: schemas.NameAgeListCreate):
    db_peter = name_age_list.NameAgeListTable(name=nameagelist.name, age=nameagelist.age)
    db.add(db_peter)
    db.commit()
    db.refresh(db_peter)

    return db_peter