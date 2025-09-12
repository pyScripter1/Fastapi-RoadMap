"""
Доступ к заголовкам запросов и ответов
Для получения заголовков запроса применяется класс fastapi.Header. Например, получим заголовок User-Agent:
"""

from fastapi import FastAPI, Header, Response

app = FastAPI()


@app.get("/")
def root(user_agent: str = Header()):
    return {"User-Agent": user_agent}

"""
Для отправки заголовка в конструктор класса Response или
его наследников параметру headers передается словарь, где ключи представляют названия заголовков:
"""

@app.get("/root")
def get_root():
    data = "Hello world"
    return Response(content=data, media_type="text/plain", headers={"Secret-Code" : "123456"})

"""
Также можно задать заголовки с помощью атрибута headers, который есть у класса Response и его наследников.
Данный атрибут фактически представляет словарь, где ключи - названия заголовков:
"""

@app.get("/resp")
def get_resp(response : Response):
    response.headers["Secret-Code"] = "12345"
    return {"message" : "Hello from my api"}

