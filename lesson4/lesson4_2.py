# переадресация

# Для переадресации в приложении FastAPI применяется класс RedirectResponse
# (класс-наследник от Response). В качестве обязательного параметра конструктор RedirectResponse
# принимает адрес для перенаправления:

from fastapi import FastAPI
from fastapi.responses import RedirectResponse, PlainTextResponse

app = FastAPI()

@app.get("/old")
async def old():
    return RedirectResponse("/new") # перенаправляем по пути /new

"""
альтернативный вариант:
@app.get("/old", response_class= RedirectResponse)
def old():
    return "/new"
"""

# В данном случае при обращении по пути "/old" происходит перенаправление по пути "/new". Альтернативный вариант:
@app.get("/new", response_class=PlainTextResponse)
async def new():
    return "New page"

# также можно перенаправлять по абсолютному пути:
@app.get("/pyscipter", response_class=RedirectResponse)
async def pyscripter():
    return "https://github.com/pyScripter1/Fastapi-RoadMap"


