from pathlib import Path
from urllib import request

from database import get_db
from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from models import crud, dbSchemas, schemas
from passlib.context import CryptContext
# from pydantic.main import BaseModel
from sqlalchemy.orm import Session

# from routers.authentication import *


router = APIRouter()


templates = Jinja2Templates(directory="./templates")


# formのページ用意
@router.get("/{id}", response_class=HTMLResponse)
async def show_HTML(request: Request, id: str):
    return templates.TemplateResponse("index.html", {"request": request, "id": id})


# formデータの送信
@router.post("/postForm")
async def postForm(username: str = Form(...), password: str = Form(...)):
    return {"username": username, "password": password}