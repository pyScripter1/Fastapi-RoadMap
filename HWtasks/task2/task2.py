# Создать fastapi приложение, в котором реализовать 4 get-конечных точек
# /hello, /index, /html, /json
# в которых возвращать текст, html документ, html тэг, json объект соответственно

from fastapi import FastAPI
from fastapi.responses import FileResponse, HTMLResponse, PlainTextResponse, JSONResponse

app = FastAPI()

@app.get("/hello")
def get_hello():
    return PlainTextResponse("Это просто текст с hello")

@app.get("/index")
def get_index():
    return FileResponse("HWtasks/task2/index.html")

@app.get("/html")
def get_html():
    return HTMLResponse("<h1>Это html тег</h1>")

@app.get("/json")
def get_json():
    return JSONResponse(content={"message": "Hello world"})
