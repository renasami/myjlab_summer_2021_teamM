from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from models import crud, tasks, schemas
from models.database import session, ENGINE



app=FastAPI()
tasks.Base.metadata.create_all(bind=ENGINE)

def get_db():
    try:
        db = session()
        yield db
    finally:
        db.close()
        print('closed database')



class MyPostData(BaseModel):
    name: str
    mean: str

origins = [
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# テスト用辞書
test_data = {
    "pachinko": "玉を弾く遊び",
    "slot": "リールを回す遊び",
}

@app.get("/")
async def index():
    return {"message": "hello world"}


@app.get("/data/")
def read_data(key: str):
    return test_data[key]


@app.post("/data/")
def update_data(post_data: MyPostData):
    test_data[post_data.name] = post_data.mean
    return {"message": "post success!!"}




@app.get("/test_task")
def get_task(db: Session = Depends(get_db)):
    tasks = crud.get_tasks(db)
    return tasks

@app.post("/test_task")
def create_task(task: schemas.TestTaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db=db, task=task)



if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


    