from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from .database import Base
from datetime import datetime

# テーブル定義(DBのモデル)
# class テーブル名Table(Base):
    # __tablename__ = 'テーブル名'
    # 定義されている全てのカラムを記述


# class LIKESTable(Base):
#     __tablename__ = 'LIKES'
#     ID = Column(Integer, primary_key=True, autoincrement=True)
#     POST_ID = Column(Integer) 
#     USER_ID = Column(Integer)


#     def __repr__(self):
#         return f'<LIKESTable {self.ID} {self.POST_ID} {self.USER_ID}>'


#     def toDict(self):
#         return {
#             'ID':self.ID,
#             'POST_ID':self.POST_ID,
#             'USER_ID':self.USER_ID
#         }
