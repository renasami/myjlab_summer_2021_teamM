from sqlalchemy.orm import Session, session
from . import tasks, schemas, users, tasks, musics,  posts #テーブルをつくったらここにモジュール追加

# 全てのCRUD処理をここに記述。
# CRUD名_テーブル名


def get_tasks(db: Session):
    return db.query(tasks.TestTasksTable).all()

def create_task(db: Session, task: schemas.TestTaskCreate):
    db_task = tasks.TestTasksTable(name=task.name, content=task.content)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)

    return db_task

def get_login_list(db: Session):
    return db.query(users.USERSTable).all()

# #ユーザー情報取得
# USER_LOGIN_LIST = Session.query(USERS.USER_ID,USERS.MAIL, USERS.PASSWORD)


# ログインしているかの確認 --- (*2)
def is_login():
    return 'login' in session


# ログインを試行する
def try_login(db: Session):
    USER_LOGIN_LIST = get_login_list(db)
    mail = "kaiseiota0620@gmail.com"
    password = "peter555"
    print('入力されたメールアドレス'+ mail)
    print('入力されたパスワード' + password)
    userlen = len(USER_LOGIN_LIST)

    for i in range(userlen):
        print('ユーザーリストのmail' + USER_LOGIN_LIST[i]['MAIL'])
        print('ユーザリストのpassword' +USER_LOGIN_LIST[i]['PASSWORD'])
        if mail != USER_LOGIN_LIST[i]['MAIL'] and password != USER_LOGIN_LIST[i]['PASSWORD']:
            print('存在しません。')

        elif mail == USER_LOGIN_LIST[i]['MAIL'] and password != USER_LOGIN_LIST[i]['PASSWORD']:
            print('入力したパスワードが間違っています。')

        elif mail != USER_LOGIN_LIST[i]['MAIL'] and password == USER_LOGIN_LIST[i]['PASSWORD']:
            print('入力したメールアドレスが間違っています。')
        else:
            session['login'] = user
            return True

# @app.route('/login/try', methods=['POST'])
# def login_try():
#     ok = try_login(request.form)

#     if not ok: return msg('ログイン失敗')
#     return redirect('/') #戻り値は好きに変えてください


# 新規登録
# @app.route('/register/try', medhods=['POST'])
# def register_try():
#     res = {}
#     res['mail'] = request.form.get('mail')
#     res['pw'] = request.form.get('pw')

#     exec('''
#     INSERT INTO USERS (MAIL, PASSWORD)
#     VALUES(?, ?)''',
#     res['mail'], res['pw'])

#     return redirect('/login')

#ログアウト

def try_logout():
    session.pop('login', None)

# @app.route('/logout')
# def logout():
#     user.try_logout()
#     return msg('ログアウトしました')



