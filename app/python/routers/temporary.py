# @app.get("/searchforsession")
# def search_session(db: Session = Depends(get_db)):
#     mail = "kaisei@gmail.com"
#     searchinfo = crud.search_mail(db, mail)

#     return searchinfo

# @app.get("/user")
# def get_index(username: str = Depends(auth.verify_token)):
#     print("get_index: %s" % username)
#     return {"username": username}


#ログイン試行
# @app.post('/login')
# def login_try(db: Session = Depends(get_db)):
#     can_login = crud.try_login(db)
#     ok = crud.try_login(request.form, db)


#ログイン試行

# @app.get('/users')
# def check(db: Session = Depends(get_db)):
#     test = crud.try_login(db)

#     return test

# @app.get('/User')
# def get_login_list(db: Session = Depends(get_db)):
#     user = crud.get_login_list(db)
#     for row in user:
#         d = row.__dict__
#     typed = type(d)
#     return d['MAIL'], typed


# @app.get("/movie")
# # 動画ファイルを受け取る upfileと仮定
# def get_movie():

#     #動画ファイルを受け取る処理書く、でもわからん。
    # upfile = 
#     # 受け取ったファイル形式をチェック、mp4ファイルだけを許可
#     if not re.search(r'\.(mp4)$', upfile.filename):
#         print('mp4ファイルではない:', upfile.filename)
#         return 0


# @app.get('/movie')
# # 動画ファイルをmoviesテーブルのidと同じ数字にリネームする
# def rename_movie():

#     namefile = ムービーid

#     renamedfile = os.rename(upfile, namefile)

#     return renamedfile



# @app.get("/fileupload")
# async def fileupload(request: Request):
#     '''docstring
#     ファイルアップロード(初期表示)
#     '''
#     html_content = """
#     <html>
#         <head>
#             <title>Some HTML in here</title>
#         </head>
#         <body>
#             <h1>Look ma! HTML!</h1>
#             <form method=post action="/fileupload/upload">
#                 <p>アップロードするファイルを選択してください.</p>
#                 <p><input type="file"></p>
#                 <input type="submit" value="アップロード">
#             <form>
#         </body>
#     </html
#     """
#     return HTMLResponse(content=html_content, status_code=200)

# @app.post("/fileupload/upload")
# async def image(file: UploadFile = File(...)):
#     global upload_folder
#     print("1")

#     file_object = file.file

#     print("2")

#     upload_folder = open(os.path.join(upload_folder, file.filename), 'wb+')

#     print("3")
#     shutil.copyfileobj(file_object, upload_folder)

#     print("4")

#     upload_folder.close()

#     print("5")

#     return {'filename': file.filename}



# # 自分がいいねした動画のみをすべて取得
# def get_Mylikemovie(db: Session = Depends(get_db)):
    
#     mylike = crud.get_mylikemovie(db) 

#     return mylike

# @app.get("/get_url")
# def get_youtube(db: Session = Depends(get_db)):

#     urlyoutube = crud.get_allyoutube(db)
#     url = urlyoutube.__str__
    
#     return type(url)

# @app.get("/get_oneURL")
# def get_Oneyoutube(db: Session = Depends(get_db)):

#     postid = 7
#     oneurl = crud.get_youtube(db, postid)
#     embedURL = "https://www.youtube.com/embed/" + oneurl[0]["YOUTUBE"]

#     return embedURL

#URLID_LIST
#{
# url:star,
# movie_id: int
#}
#
#

# @app.get("/qr")
# def make_qr():
#     file_name = FILES_DIR +'test.png'
#     qr = "https://www.youtube.com/watch?v=Fa1UPDtZBYY"
#     img = qrcode.make(qr)
#     img.save(file_name)

#     return
#自分のいいねした投稿を返す

# @app.get('/get_mylike')
# def get_Mylike(db: Session = Depends(get_db)):
#     mylikelist = []
#     myyoutubelist = []
#     user_id = 1
#     useralllike = crud.get_user_like(db, user_id)
    
    
#     for idx in range(len(useralllike)):
#        mylikelist.append(useralllike[idx]["POST_ID"])


#     for i in range(len(mylikelist)):
#         mylikepost = crud.get_mylikeyoutube(db, mylikelist[i])

#     # for x in range(len(mylikelist)):
#     #     youtubeurl = mylikelist[x]["YOUTUBE"].

#     return mylikepost









# いいね機能テストコード
# @app.post('/users/{user_id}/likes/')
# def create_likes_for_user(like: schemas.LikesCreate,db: Session = Depends(get_db)):
#     user_id=1
#     post_id=1
#     return crud.create_user_like(db=db, like=like, user_id=user_id, post_id=post_id)



# @app.post('/post_like')
# def post_like(button: CreateLikeinfo, likes=schemas.LikesCreate,db: Session = Depends(get_db)):
#     user_id = button.user_id
#     postid = button.postid

#     return crud.create_user_like(db=db, user_id=user_id, likes=likes, postid=postid)


# @app.websocket("/ws")
# async def websocket_endpoint(ws: WebSocket):
#     await ws.accept
#     #クライアントを識別するためのIDを取得
#     key = ws.headers.get('sec-websocket-key')
#     clients[key] = ws
#     try:
#         while True:
#             # クライアントからメッセージを受信, 
#             # data = await ws.receive_text()
#             receivelike = await crud.create_user_like(db=db)

#             # 接続中のクライアントそれぞれにメッセージを送信(ブロードキャスト)
#             for client in clients.values():
#                 await cnt_getlike()
#     except:
#         await ws.close()
#         #接続切れた場合、当該クライアントを削除する
#         del clients[key]


# @app.get("/test_task")
# def get_task(db: Session = Depends(get_db)):
#     tasks = crud.get_tasks(db)
#     return tasks

# @app.post("/test_task")
# def create_task(task: schemas.TestTaskCreate, db: Session = Depends(get_db)):
#     return crud.create_task(db=db, task=task)



