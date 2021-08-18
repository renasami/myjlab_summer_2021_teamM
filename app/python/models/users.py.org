from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from .database import Base
import datetime
# from datetime import datetime

# テーブル定義(DBのモデル)
# class テーブル名Table(Base):
    # __tablename__ = 'テーブル名'
    # 定義されている全てのカラムを記述


class USERSTable(Base):
    __tablename__ = 'USERS'
    ID = Column(Integer, primary_key=True, autoincrement=True) 
    PASSWORD = Column(String(1000)) 
    CREATED_AT = Column(DateTime, default=datetime.datetime.now(), nullable=False)
    UPDATED_AT = Column(DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now(), nullable=False)
    MAIL = Column(String(100))

    def __repr__(self):
        return f'<USERTable {self.ID} {self.PASSWORD} {self.CREATED_AT} {self.UPDATED_AT} {self.MAIL}>'


    def toDict(self):
        return {
            'ID':self.ID,
            'PASSWORD':self.PASSWORD,
            'CREATED_AT':self.CREATED_AT,
            'UPDATED_AT':self.UPDATED_AT,
            'MAIL':self.MAIL
        } 