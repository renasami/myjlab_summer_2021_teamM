from sqlalchemy import Column, Integer, String
from .database import Base

# テーブル定義(DBのモデル)
# class テーブル名Table(Base):
    # __tablename__ = 'テーブル名'
    # 定義されている全てのカラムを記述


class TestTasksTable(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    content = Column(String(128), nullable=False)

