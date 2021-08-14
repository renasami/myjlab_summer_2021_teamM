from os import getenv
from hashlib import pbkdf2_hmac
from secrets import token_hex
from fastapi import APIRouter, Header, Depends, HTTPException,FastAPI
from pydantic import BaseModel

router = APIRouter()

users = {
    "foo": "d7277d65c13dbd72e4b2d3ce66a56dd70fb5a0fea0bec058dc8e313fc743c12c",
    "bar": "466b21c4b915616bf9d69696bc1da7c0f819daa7371dadbecfd4d542d7e8b8a2",
}

session = {}


class Credentials(BaseModel):
    username: str
    password: str


def hash_password(password: str) -> str:
    return pbkdf2_hmac("sha256", password.encode(), getenv("SALT").encode(), 100000).hex()


def get_token_header(authorization: str = Header()):
    print(authorization)
    if authorization is None:
        raise HTTPException(401, headers={"WWW-Authenticate": 'Bearer realm=""'})
    if authorization[:7] != "Bearer ":
        raise HTTPException(400)
    return authorization[7:]


def verify_token(token: str = Depends(get_token_header)):
    if token not in session:
        raise HTTPException(401, headers={"WWW-Authenticate": 'Bearer error="invalid_token"'})
    return session[token]


@router.post("/signup")
def post_auth_signup(c: Credentials):
    if c.username in users:
        raise HTTPException(409)
    # TODO check password policy
    users[c.username] = hash_password(c.password)
    token = token_hex()
    session[token] = c.username
    print(session)
    return {"token": token}


@router.post("/signin")
def post_auth_signin(c: Credentials):
    print(c)
    if c.username not in users:
        raise HTTPException(404)
    if users[c.username] != c.password:
        raise HTTPException(401, headers={"WWW-Authenticate": 'Bearer error="invalid_request"'})
    token = token_hex()
    session[token] = c.username
    print(session)
    return {"token": token}


@router.post("/signout")
def post_auth_signout(token: str = Depends(get_token_header)):
    if token in session:
        del session[token]


# @app.get("/user")
# def get_index(username: str = Depends(verify_token)):
#     return {"username": username}