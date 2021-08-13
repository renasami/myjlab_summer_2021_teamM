from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from .database import Base
from datetime import datetime

# テーブル定義(DBのモデル)
# class テーブル名Table(Base):
    # __tablename__ = 'テーブル名'
    # 定義されている全てのカラムを記述


class COMMENTSTable(Base):
    __tablename__ = 'COMMENTS'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    COMMENT = Column(String(20)) 
    POST_ID = Column(Integer, nullable=False, ForeignKey("POSTS.ID")) 
    USER_ID = Column(Integer, nullable=False, ForeignKey("USERS.ID"))
    CREATED_AT = Column(DateTime, default=datetime.now(), nullable=False)
    UPDATED_AT = Column(DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=False)