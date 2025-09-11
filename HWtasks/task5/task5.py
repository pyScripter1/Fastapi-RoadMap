from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, Field


app = FastAPI()

class UserCreate(BaseModel):
    name : str
    email : EmailStr
    age : int | None = Field(default=None, gt=0)
    is_subscribed : bool = False

def check_user_age(user : UserCreate) -> UserCreate:
    if user.age is None:
        user.age = None
    return user

@app.post("/create_user")
def create_user(user : UserCreate):
    user_info = check_user_age(user).model_dump()
    return user_info