from fastapi import FastAPI, Cookie, Response, Request
from pydantic import BaseModel
from uuid import uuid4

app = FastAPI()

class User(BaseModel):
    username : str
    password : str

fake_db = [
    {
        "username" : "Daniil123",
        "password" : "123123"
    },
    {
        "username" : "Igor123",
        "password" : "qwerty"
    }
]

@app.post("/login")
def login(user : User, response : Response):
    for login_user in fake_db:
        if login_user["username"] == user.username and login_user["password"] == user.password:
            response.set_cookie(key="session_token", value=str(uuid4()), httponly=True)
            return {"message" : f"Authorization for {user.username}"}
    return {"message" : "Unauthorized"}

@app.get("/user")
def get_cookie(request : Request):
    session_token = request.cookies.get("session_token", "invalid_token_value")
    return {"session_token" : session_token}

