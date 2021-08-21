from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from .database import Base
from datetime import datetime

# テーブル定義(DBのモデル)
# class テーブル名Table(Base):
    # __tablename__ = 'テーブル名'
    # 定義されている全てのカラムを記述


class POSTSTable(Base):
    __tablename__ = 'POSTS'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    USER_ID = Column(Integer)
    YOUTUBE = Column(String(100))
    CAPTION = Column(String(200)) 
    TITLE = Column(String(30))
    YOUTUBE = Column(String(100))
    CREATED_AT = Column(DateTime, default=datetime.now(), nullable=False)
    UPDATED_AT = Column(DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=False)

    def __repr__(self):
        return f'<POSTSTable {self.ID} {self.USER_ID} {self.YOUTUBE} {self.CAPTION} {self.TITLE} {self.YOUTUBE} {self.CREATED_AT} {self.UPDATED_AT} ' 

    def toDict(self):
        return {
            'ID': self.ID,
            'USER_ID': self.USER_ID,
            'YOUTUBE':self.YOUTUBE,
            'CAPTION':self.CAPTION,
            'TITLE':self.TITLE,
            'YOUTUBE':self.YOUTUBE,
            'CREATED_AT':self.CREATED_AT,
            'UPDATED_AT':self.UPDATED_AT,
        }
