from fastapi import FastAPI, Body
from fastapi.responses import FileResponse, HTMLResponse

app = FastAPI() # создаем приложение

@app.get("/") # корневой путь
def root():
    return FileResponse("lesson5/calculate.html")

# Для получения данных из тела запроса можно использовать класс Body из пакета fastapi.
# Данный класс позволяет связать с параметром функции-обработчика запроса либо все тело запроса,
# либо какие-то отдельные его значения.

@app.post("/sum") # пост запрос из calculate.html
def total(data = Body()):
    a = data["num_a"]
    b = data["num_b"]
    print(int(a) + int(b))
    return {"message" : f"Результат: {int(a) + int(b)}"}

@app.post("/sub")
def sub(data = Body()):
    a = data["num_a"]
    b = data["num_b"]
    return {"message" : f"Результат: {int(a) - int(b)}"}

@app.post("/mult")
def mult(data = Body()):
    a = data["num_a"]
    b = data["num_b"]
    return {"message" : f"Результат: {int(a) * int(b)}"}

@app.post("/div")
def sub(data = Body()):
    a = data["num_a"]
    b = data["num_b"]
    if b == "0":
        return {"message" : "Zero Division"}
    return {"message" : f"Результат: {int(a) / int(b)}"}