from sqlalchemy import create_engine
# from models.tasks import Base
# from models.test import Base
from models.users import Base
from models.posts import Base
from models.likes import Base
from models.comments import Base

# dbコンテナにテーブルをつくるときに back_container上のターミナルで"python -m createdatabase"とうつと
# dbコンテナにテーブルが作成される



host = "db:3306"
db_name = "vue-fastapi-db"
user = "fastapi"
password = "secret"

# host = "host.docker.internal:3307"
# db_name = "vue_fastapi_db"
# user = "root"
# password = "myjdbroot"



DATABASE = 'mariadb://%s:%s@%s/%s?charset=utf8' % (
    user,
    password,
    host,
    db_name,
)

ENGINE = create_engine(
    DATABASE,
    encoding="utf-8",
    echo=True
)

def reset_database():
    Base.metadata.drop_all(bind=ENGINE)
    Base.metadata.create_all(bind=ENGINE)


if __name__ == "__main__":
    reset_database()