# Ваша задача состоит в том, чтобы расширить существующее приложение FastAPI, добавив новую конечную точку POST, которая принимает данные JSON, представляющие пользователя, и возвращает те же данные с дополнительным полем, указывающим, является ли пользователь взрослым или нет.
#
# 1. Определите Pydantic модель с именем "Пользователь" ("User") со следующими полями:
#
#    - `name` (str)
#
#    - `age` (int)
#
# 2. Создайте новый маршрут `/user`, который принимает запросы POST и принимает полезную нагрузку JSON, содержащую пользовательские данные, соответствующие модели `User`.
#
# 3. Реализуйте функцию для проверки того, является ли пользователь взрослым (возраст >= 18) или несовершеннолетним (возраст < 18).
#
# 4. Верните пользовательские данные вместе с дополнительным полем `is_adult` в ответе JSON, указывающим, является ли пользователь взрослым (True) или несовершеннолетним (False).

# Пример:
# Запрос в формате JSON:
#
# {
#     "name": "John Doe",
#     "age": 25
# }
# Ответ в формате JSON:
#
# {
#     "name": "John Doe",
#     "age": 25,
#     "is_adult": true
# }

from fastapi import FastAPI, Form
from fastapi.responses import FileResponse
from pydantic import BaseModel

class User(BaseModel):
    age : int
    name : str


app = FastAPI()

@app.get("/users")
def get_users():
    return FileResponse("HWtasks/task1/check_user.html")

@app.post("/users")
def check_user(username = Form(), userage = Form()):
    result = {
        "name" : username,
        "age" : userage,
        "is_adult" : int(userage) >= 18
    }
    return result