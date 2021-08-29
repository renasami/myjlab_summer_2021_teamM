"""dbのスキーマ定義

Todo:
    * クラスがBaseを全て継承していてIDやDictなど共通項が多いためBaseを継承したTableBaseClassの作成。
    クラスがくどい。
    * クラスに__repr__しか書いてないのは何か意図があってのこと?__str__も追記したほうがわかりやすくなるかと↑が終わってからだけど

"""


from .database import Base
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from datetime import datetime
# テーブル定義(DBのモデル)
# class テーブル名Table(Base):
    # __tablename__ = 'テーブル名'
    # 定義されている全てのカラムを記述


#TODO:


#loginuser Info
class LoginUserInfo:
    username: str
    password: str

#ユーザ
class UsersTable(Base):
    __tablename__ = 'USERS'
    ID = Column(Integer, primary_key=True, autoincrement=True) 
    PASSWORD = Column(String(1000)) 
    CREATED_AT = Column(DateTime, default=datetime.now(), nullable=False)
    UPDATED_AT = Column(DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=False)
    MAIL = Column(String(100))
    """UsresTable

    ユーザー情報格納のためのクラス。

    Attributes:
        ID (int): 基本的にautoincrementだと思われる
        PASSWORD(str):パスワード(ハッシュ値を格納する予定)
        CREATED_AT(datetime):作成日
        UPDATED_AT(datetime):更新日
        MAIL(str):e-mailアドレス
        属性の名前 (:obj:`属性の型`): 属性の説明.

    """
    #復元意図があるからreperなのかな
    def __repr__(self):
        return f'<USERTable {self.ID} {self.PASSWORD} {self.CREATED_AT} {self.UPDATED_AT} {self.MAIL}>'


    def toDict(self):
        """辞書化関数
        Args: 
            self:自己参照
        Returns: 
            dict: classのattrを辞書として返す。
        """
        return {
            'ID':self.ID,
            'PASSWORD':self.PASSWORD,
            'CREATED_AT':self.CREATED_AT,
            'UPDATED_AT':self.UPDATED_AT,
            'MAIL':self.MAIL
        } 

#いいね
class LikesTable(Base):
    __tablename__ = 'LIKES'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    POST_ID = Column(Integer) 
    USER_ID = Column(Integer)
    """LikesTable

    いいね情報の保存のためのクラス

    Attributes:
        ID (int): 基本的にautoincrementだと思われる
        POST_ID(int): 投稿のid (=PostTable[ID])
        USER_ID(int): いいねしたユーザのID (=UsersTable[ID])

    """


    def __repr__(self):
        """rep

        eval関数で復元可能なオブジェクトとして返す。
        Args: 
            self:自己参照
        Returns:
            Obj:__repr__オブジェクト

        """

        return f'<LIKESTable {self.ID} {self.POST_ID} {self.USER_ID}>'


    def toDict(self):
        return {
            'ID':self.ID,
            'POST_ID':self.POST_ID,
            'USER_ID':self.USER_ID
        }

#コメント
class CommentsTable(Base):
    __tablename__ = 'COMMENTS'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    POST_ID = Column(Integer) 
    USER_ID = Column(Integer)
    COMMENTS = Column(String(100)) 
    CREATED_AT = Column(DateTime, default=datetime.now(), nullable=False)
    UPDATED_AT = Column(DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=False)
    """CommentsTable

    コメント情報の保存のためのクラス

    Attributes:
        ID (int): 基本的にautoincrementだと思われる
        POST_ID(int): 投稿のid (=PostTable[ID])
        USER_ID(int): コメントしたユーザのID (=UsersTable[ID])
        COMMENTS(str):コメント内容、上限100文字
        CREATED_AT(datetime):作成日
        UPDATED_AT(datetime):更新日
    """


    def __repr__(self):
        return f'<COMMENTSTable {self.ID} {self.POST_ID} {self.USER_ID} {self.COMMENTS} {self.CREATED_AT} {self.UPDATED_AT}>'

    def toDict(self):
        return {
            'ID':self.ID,
            'POST_ID':self.POST_ID,
            'USER_ID':self.USER_ID,
            'COMMENTS':self.COMMENTS,
            'CREATED_AT':self.CREATED_AT,
            'UPDATED_AT':self.UPDATED_AT
        }

#投稿
class PostTable(Base):
    __tablename__ = 'POSTS'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    USER_ID = Column(Integer)
    YOUTUBE = Column(String(100))
    CAPTION = Column(String(200)) 
    TITLE = Column(String(30))
    YOUTUBE = Column(String(100))
    CREATED_AT = Column(DateTime, default=datetime.now(), nullable=False)
    UPDATED_AT = Column(DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=False)

    """PostTable

    投稿情報のためのクラス

    Attributes:
        ID (int): 基本的にautoincrementだと思われる
        USER_ID(int): 投稿したユーザのID (=UsersTable[ID])
        YOUTUBE(str):youtubeのurl TODO:確実に100文字じゃ足りない
        CAPTION(str):サムネのurl TODO:同上
        TITLE(str):タイトル、上限30文字
        YOUTUBE(str):youtubeのurl TODO:消せ
        CREATED_AT(datetime):作成日
        UPDATED_AT(datetime):更新日
    """


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



#これは多分テストコード
class TestTasksTable(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    content = Column(String(128), nullable=False)