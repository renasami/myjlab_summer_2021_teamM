# from app.python.models.database import DATABASE
from models.database import DATABASE
from typing import List
from pydantic import BaseModel
from datetime import datetime

# モデル定義(fastapiのモデル)
# class テーブル名Base(BaseModel):
#     使用するカラムを記述

# class テーブル名処理名(テーブル名Base):
#     pass

#     class Config:
#         orm_mode = True


#users
class UsersBase(BaseModel):
    mail: str
    password: str
    created_at: datetime
    updated_at: datetime

class UsersCreate(BaseModel):
    mail: str
    password: str
    class Config:
        orm_mode = True


class Users(UsersBase):

    mail: str 
    password: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

#end users


#posts
class PostsBase(BaseModel):
    user_id: int
    youtube: str
    caption: str
    title: str

class PostsCreate(PostsBase):
    pass
    
    class Config:
        orm_mode = True


class Posts(PostsBase):
    thumbnail_id: str
    user_id: int
    caption: str
    title: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

#end posts

#likes
class LikesBase(BaseModel):
    post_id: int
    user_id: int

class LikesCreate(LikesBase):
    pass
    
    class Config:
        orm_mode = True


class Likes(LikesBase):
    post_id: int
    user_id: int

    class Config:
        orm_mode = True

#end likes

#commnet
class CommentsBase(BaseModel):
    post_id: int
    user_id: int
    comments: str
    created_at: datetime
    updated_at: datetime

class CommentsCreate(CommentsBase):
    pass
    
    class Config:
        orm_mode = True


class Comments(CommentsBase):
    post_id: int
    user_id: int
    comments: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

#end comment


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


#movies
class MoviesBase(BaseModel):
    moviepath: str
    post_id: int
    user_id: int


class MoviesSend(MoviesBase):
    pass
    
    class Config:
        orm_mode = True


class Movies(MoviesBase):
    moviepath: str
    post_id: int

    class Config:
        orm_mode = True

#end