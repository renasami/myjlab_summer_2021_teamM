
from models.database import session, ENGINE
def get_db():
    try:
        db = session()
        yield db
    finally:
        db.close()
        print('closed database')