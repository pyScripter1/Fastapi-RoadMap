# получение списков

from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field

class Person(BaseModel):
    name : str
    age : int

app = FastAPI()

@app.get("/")
def root():
    return FileResponse("lesson6/main.html")

@app.post("/hello")
def post_root(people: list[Person]):
    return {"message" : people}

# получение вложенных списков
from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel


class Person(BaseModel):
    name: str
    languages: list = []


app = FastAPI()


@app.get("/")
def root():
    return FileResponse("public/index.html")


@app.post("/hello")
def hello(person: Person):
    return {"message": f"Name: {person.name}. Languages: {person.languages}"}

# В данном случае для хранения языков в классе Person определен атрибут languages.
# В этом случае отправка данных из javascript выглядела бы следующим образом:
"""
const response = await fetch("/hello", {
    method: "POST",
    headers: { "Accept": "application/json", "Content-Type": "application/json" },
    body: JSON.stringify({ 
        name: "Tom",
        languages: ["Python", "JavaScript"]
    })
});
const data = await response.json();
console.log(data);      // {message: "Name: Tom. Languages: ['Python', 'JavaScript']"}
"""


# Вложенные модели
# Одна модель может содержать другую модель. Например, пользователь работает в какой-нибудь компании.
# И для хранения данных компании можно создать отдельную модель - Company:


from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel


class Company(BaseModel):
    name: str


class Person(BaseModel):
    name: str
    company: Company


app = FastAPI()


@app.get("/")
def root():
    return FileResponse("public/index.html")


@app.post("/hello")
def hello(person: Person):
    return {"message": f"{person.name} ({person.company.name})"}

