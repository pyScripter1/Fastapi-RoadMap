# В прошлой теме рассматривалось получение данных из тела запроса с помощью класса
# fastapi.Body в виде словаря или отдельных его значений. Однако FastAPI также позволяет получать данные
# в виде объектов своих классов. Такие классы должны быть унаследованы от класса pydantic.BaseModel.
# Такие классы определяются специально под запрос, данные которого необходимо получить.

from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field

# класс Field нужен для детальной настройки атрибутов моделей

# определим класс
class Person(BaseModel):
    name : str
    age : int | None = None# делаем данное поле необязательным

class User(BaseModel):
    name : str = Field(default="NoName", min_length=2, max_length=20)
    age : int = Field(default=0, gt=17, lt=111)

app = FastAPI()

@app.get("/", response_class=FileResponse)
def root():
    return "lesson6/index.html"

@app.post("/hello")
def post_root(person: Person):
    if person.age == None:
        return {"message" : f"Name: {person.name}"}
    else:
        return {"message" : f"Name: {person.name}, age: {person.age}"}

@app.get("/index", response_class=FileResponse)
def second_root():
    return "lesson6/index2.html"

@app.post("/hello2")
def second_post(user: User):
    return {"message" : f"User: {user.name}, age: {user.age}"}