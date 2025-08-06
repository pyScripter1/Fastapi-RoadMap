# Отправка заголовков
# Для отправки заголовка в конструктор класса
# Response или его наследников параметру headers передается словарь, где ключи представляют названия заголовков:

from fastapi import FastAPI, Response

app = FastAPI()

@app.get("/")
def root():
    data = "Hello world"
    return Response(content=data, media_type="text/plain", headers={"Secret-Code" : "123458"})

# Для примера в данном случае клиенту отправляется кастомный заголовок "Secret-Code" со значением "123459"


# Также можно задать заголовки с помощью атрибута headers, который есть у класса Response и его наследников.
# Данный атрибут фактически представляет словарь, где ключи - названия заголовков:
@app.get("/test")
def test(response: Response):
    response.headers["Secret-Code"] = "123123"
    return {"message" : "Hello Daniil"}

