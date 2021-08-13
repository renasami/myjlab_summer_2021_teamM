from sqlalchemy import Column, Integer, String
from .database import Base

# テーブル定義(DBのモデル)
# class テーブル名Table(Base):
    # __tablename__ = 'テーブル名'
    # 定義されている全てのカラムを記述


class NameAgeListTable(Base):
    __tablename__ = 'name_age_list'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(30), nullable=False)
    age = Column(Integer, nullable=False)

