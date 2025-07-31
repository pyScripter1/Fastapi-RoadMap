# Одной из расспространненых задач в веб-приложении является отправка статусных кодов, которые указывают на статус выполнения операции на сервере.
#
# 1xx: предназначены для информации. Ответ с таким кодом не может иметь содержимого
#
# 2xx: указывает на успешноее выполнение операции
#
# 3xx: предназначены для переадресации
#
# 4xx: предназначены для отправки информации об ошибок клиента
#
# 5xx: предназначены для информации об ошибках сервера
#
# По умолчанию функции обработки отправляют статусный код 200,
# но при необходимости мы можем отправить любой статусный код. Для этого у методов
# get(), post(), put(), delete(), options(), head(), patch(), trace()
# в классе FastAPI применяется параметр status_code, который принимает числовой код статуса HTTP.

from fastapi import FastAPI, status
from fastapi.responses import HTMLResponse, JSONResponse
# status - модуль, в котором константы для статусных кодов

app = FastAPI()

# метод get с параметром status_code=404
@app.get("/notfound", status_code=404)
async def notfound():
    return {"message" : "NotFoundError"}

# при обращении по пути /notfound клиенту отправляется статусный код ошибки

@app.get("/error", status_code=status.HTTP_404_NOT_FOUND, response_class=HTMLResponse)
async def error():
    return "<h1>404 Not found Error</h1>"

# при обращении по пути /error будет html тег 404 Not found Error


@app.get("/new_error")
def notfound():
    return JSONResponse(content={"message": "Resource Not Found"}, status_code=404)