# получение данных отдельных значений
# в lesson5_1, lesson5 мы рассмотрели примеры получения данных из тела запроса в один параметр
# Однако, установив параметр embed=True, можно получать отдельные значения:

from fastapi import FastAPI, Body
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/index", response_class=FileResponse)
def root():
    return "lesson5/index.html"

# также класс Body поддерживает валидацию данных
@app.post("/hello")
def hello(name: str=Body(embed=True, min_length=3, max_length=20), age: int=Body(embed=True, gt=17, lt=111)):
    return {"message" : f"This is {name} and {age}"}


