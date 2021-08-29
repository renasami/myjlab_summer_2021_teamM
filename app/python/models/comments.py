from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from .database import Base
from datetime import datetime

# テーブル定義(DBのモデル)
# class テーブル名Table(Base):
    # __tablename__ = 'テーブル名'
    # 定義されている全てのカラムを記述


# class COMMENTSTable(Base):
#     __tablename__ = 'COMMENTS'
#     ID = Column(Integer, primary_key=True, autoincrement=True)
#     POST_ID = Column(Integer) 
#     USER_ID = Column(Integer)
#     COMMENTS = Column(String(100)) 
#     CREATED_AT = Column(DateTime, default=datetime.now(), nullable=False)
#     UPDATED_AT = Column(DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=False)


#     def __repr__(self):
#         return f'<COMMENTSTable {self.ID} {self.POST_ID} {self.USER_ID} {self.COMMENTS} {self.CREATED_AT} {self.UPDATED_AT}>'

#     def toDict(self):
#         return {
#             'ID':self.ID,
#             'POST_ID':self.POST_ID,
#             'USER_ID':self.USER_ID,
#             'COMMENTS':self.COMMENTS,
#             'CREATED_AT':self.CREATED_AT,
#             'UPDATED_AT':self.UPDATED_AT
#         }
