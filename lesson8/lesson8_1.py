# получение куки
# Для получения куки на сервере применяется класс fastapi.Cookie. Например, получим выше установленную куку "last_visit":

from fastapi import FastAPI, Cookie

app = FastAPI()


@app.get("/")
def root(last_visit=Cookie()):
    return {"last visit": last_visit}

# В примере выше куки была обязательна. Если ее нет в запросе, приложение выдало бы ошибку.
# Чтобы избежать этого, мы можем определить значение по умолчанию, в том числе None:

from fastapi import FastAPI, Cookie

app = FastAPI()


@app.get("/")
def root(last_visit: str | None = Cookie(default=None)):
    if last_visit == None:
        return {"message": "Это ваш первый визит на сайт"}
    else:
        return {"message": f"Ваш последний визит: {last_visit}"}







