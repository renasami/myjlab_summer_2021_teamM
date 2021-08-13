from typing import List
from pydantic import BaseModel

# モデル定義(fastapiのモデル)
# class テーブル名Base(BaseModel):
#     使用するカラムを記述

# class テーブル名処理名(テーブル名Base):
#     pass

#     class Config:
#         orm_mode = True

class NameAgeListBase(BaseModel):
    name: str
    age: int

class NameAgeListCreate(NameAgeListBase):
    pass

    class Config:
        orm_mode = True


class NameAgeList(NameAgeListBase):
    name: str
    age: int

    class Config:
        orm_mode = True



class TestTaskBase(BaseModel):
    name: str
    content: str


class TestTaskCreate(TestTaskBase):
    pass
    
    class Config:
        orm_mode = True


class Task(TestTaskBase):
    name: str
    content: str

    class Config:
        orm_mode = True

