from app.python.models.database import DATABASE
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
    caption: str
    user_id: int
    created_at: datetime
    updated_at: datetime

class UsersCreate(UsersBase):
    pass
    
    class Config:
        orm_mode = True


class Users(UsersBase):
    caption: str
    user_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

#end users


#posts
class PostsBase(BaseModel):
    caption: str
    user_id: int
    created_at: datetime
    updated_at: datetime

class PostsCreate(PostsBase):
    pass
    
    class Config:
        orm_mode = True


class Posts(PostsBase):
    caption: str
    user_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

#end posts


#musics
class MusicsBase(BaseModel):
    music: str
    image: str
    post_id: int
    created_at: datetime
    updated_at: datetime

class MusicsCreate(MusicsBase):
    pass
    
    class Config:
        orm_mode = True


class Musics(MusicsBase):
    music: str
    image: str
    post_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

#end music

#likes
class LikesBase(BaseModel):
    post_id: int
    user_id: int
    created_at: datetime
    updated_at: datetime

class LikesCreate(LikesBase):
    pass
    
    class Config:
        orm_mode = True


class Likes(LikesBase):
    post_id: int
    user_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

#end likes

#commnet
class CommentsBase(BaseModel):
    comment: str
    post_id: int
    user_id: int
    created_at: datetime
    updated_at: datetime

class CommentsCreate(CommentsBase):
    pass
    
    class Config:
        orm_mode = True


class Comments(CommentsBase):
    comment: str
    post_id: int
    user_id: int
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