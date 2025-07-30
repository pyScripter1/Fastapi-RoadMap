# импортируем класс Fastapi для создания приложения
from fastapi import FastAPI
from fastapi.responses import FileResponse, PlainTextResponse
# По умолчанию мы можем возвращать только встроенные классы, такие как dict, list, str, int и т.д.
# Для возвращения html-страницы нам нужно импортировать класс FileResponse. Делается это вот так:
# from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/html") # get запрос по пути /html возвращает html файл
async def root_html():
    return FileResponse("lesson2/index.html") # в этот раз возвращаем html файл

@app.get("/text") # get запрос по пути /text возвращает обычный текст
async def root_text():
    return PlainTextResponse("Это просто текст и все")


# для запуска uvicorn lesson2.lesson2:app --reload
# для запуска uvicorn lesson2.lesson2:app --reload --port 8080 (если порт 8000 занят)