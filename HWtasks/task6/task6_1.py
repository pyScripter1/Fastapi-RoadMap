#.env

SECRET_KEY=ThisIsSecretKey

#config.py

from dataclasses import dataclass
from environs import Env

@dataclass
class Config:
    secret_key: str

def load_config(path: str = None) -> Config:
    env = Env()
    env.read_env(path)

    return Config(
        secret_key=env("SECRET_KEY"),
    )


#main.py

from fastapi import FastAPI, Response, Cookie
from pydantic import BaseModel
import uuid
import itsdangerous
from .config import load_config as config

users = {
    'user123': 'password123',
    'user456': 'password456'
}

tokens = {}

app = FastAPI()

class Login(BaseModel):
    username: str
    password: str

token_serializer = itsdangerous.URLSafeTimedSerializer(secret_key=config().secret_key)

@app.post('/login')
def get_session_token(login: Login, response: Response):
    if login.username in users.keys():
        if login.password == users.get(login.username, False):
            user_id = str(uuid.uuid4())
            signature = token_serializer.dumps(user_id)
            tokens[user_id] = login.username
            response.set_cookie(key="session_token", value=signature , httponly=True)
            return {"message": "Файлы Cookie установлены!"}
        else:
            return {"message": "Неверный пароль!"}
    else:
        return {"message": "Пользователь не зарегистрирован!"}


@app.get('/profile')
def check_token(session_token = Cookie()):
    date = token_serializer.loads(session_token)
    if date in tokens.keys():
        username = tokens.get(date)
        return {'username': username, 'password': users.get(username)}
    else:
        return {"message": "Unauthorized"}
