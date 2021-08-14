from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from .database import Base
from datetime import datetime

# テーブル定義(DBのモデル)
# class テーブル名Table(Base):
    # __tablename__ = 'テーブル名'
    # 定義されている全てのカラムを記述


class USERSTable(Base):
    __tablename__ = 'USERS'
    ID = Column(Integer, primary_key=True, autoincrement=True) 
    PASSWORD = Column(String(1000)) 
    CREATED_AT = Column(DateTime, default=datetime.now(), nullable=False)
    UPDATED_AT = Column(DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=False)
    MAIL = Column(String(100)) 
