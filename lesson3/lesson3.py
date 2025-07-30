from fastapi import FastAPI
from fastapi.responses import FileResponse, PlainTextResponse, HTMLResponse

app = FastAPI()


@app.get("/", response_class=FileResponse)
async def root_home(): # возвращает html файл
    return "lesson3/index.html"

@app.get("/text", response_class=PlainTextResponse)
async def root_text(): # возвращает обычный текст
    return "Это обычный текст и все"

@app.get("/html", response_class=HTMLResponse)
async def root_html(): # возвращает html код
    return "<h2>Еще одна страница</h2>"

@app.get("/parametrs/{user}-{id}") # get запрос с параметрами
async def root_parametrs(user, id):
    return {"user":user, "id":id}

