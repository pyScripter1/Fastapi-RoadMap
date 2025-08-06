# Рассмотренного в прошлых темах материала достаточно для создания примитивного приложения.
# В этой теме попробуем реализовать простейшее приложение Web API в стиле REST.
# Архитектура REST предполагает применение следующих методов или типов запросов HTTP для взаимодействия с сервером,
# где каждый тип запроса отвечает за определенное действие:
#
# GET (получение данных)
#
# POST (добавление данных)
#
# PUT (изменение данных)
#
# DELETE (удаление данных)
#
# Для каждого из этих типов запросов класс FastAPI предоставляет соответствующие методы.
# Рассмотрим, как мы можем реализовать с помощью этих методов простейший API.

import uuid
from fastapi import FastAPI, Body, status
from fastapi.responses import JSONResponse, FileResponse

# Разберем в общих чертах этот код.
# Прежде всего для представления данных, с которыми мы будем работать, определяем класс Person.

'''
Этот класс содержит три атрибута. Два атрибута - name и age будут представлять имя и 
возраст пользователя и будут устанавливаться 
через конструктор. А третий атрибут - id будет служить для уникальной идентификации данного объекта и будет хранить
 значение guid. Для генерации guid применяется функция uuid.uuid4() из пакета uuid. В конструкторе Person
  сгенерированный guid преобразуется в строку и присваивается атрибуту id.
'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.id = str(uuid.uuid4())

# имитация бд
people = [
    Person("Ivan", 34),
    Person("Aleks", 25),
    Person("George", 28)
]

# функция для поиска пользователя в бд
def find_person(id):
    for person in people:
        if person.id == id:
            return person
    return None

app = FastAPI()

# get запрос, попадаю в корень веб приложения будем открывать index.html
@app.get("/")
async def main():
    return FileResponse("lesson7/index.html")

# далее все функции которые и представляют api
# get запрос для получения всех пользователей
@app.get("/api/users")
def get_users():
    return people

# get запрос для получения пользователя по id, если пользователь не найден то возвращаем сообщение с статусом 404
# иначе возвращаем пользователя
@app.get("/api/users/{id}")
def get_person(id):
    person = find_person(id)
    if person == None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message" : "Пользователь не найден"}
        )
    return person

# post запрос для отправки данных и добавления нового пользователя
@app.post("/api/users")
def create_person(data = Body()):
    person = Person(data["name"], data["age"])
    # добавляем обект в бд
    people.append(person)
    return person

# put запрос для изменеия данных пользователя
@app.put("/api/users")
def edit_person(data = Body()):
    # получаем пользователя по id
    person = find_person(data["id"])
    if person == None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message" : "Пользователь не найден"}
        )
    # если пользователь найден, то обновляем данные
    person.age = data["age"]
    person.name = data["name"]
    return person

# запрос для удаления пользователя
@app.delete("/api/users/{id}")
def del_user(id):
    person = find_person(id)

    if person == None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message" : "Пользователь не найден"}
        )

    people.remove(person)
    return person

# Таким образом, мы определили простейший API.

