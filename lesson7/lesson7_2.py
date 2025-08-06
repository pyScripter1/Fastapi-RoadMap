# Получение заголовков
# Для получения заголовков запроса применяется класс fastapi.Header. Например, получим заголовок User-Agent

from fastapi import FastAPI, Response, Header

app = FastAPI()

@app.get("/")
def root(user_agent: str = Header(), host: str = Header()):
    return {"User-Agent" : user_agent, "Host" : host}
# При этом параметр функции, в который получаем значение заголовка, должен называться как и заголовок за тем исключением,
# что вместо дефиса применяется прочерк: параметр "user_agent" соответствует заголовку "User-Agent".



# Но в запросе может отсутствовать нужный заголовок.
# В этом случае мы можем установить для него значение по умолчанию, например, None
@app.get("/test")
def root(secret_code: str | None = Header(default=None)):
    return {"Secret-Code" : secret_code}

