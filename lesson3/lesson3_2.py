from fastapi import FastAPI, Query, Path
from fastapi.responses import PlainTextResponse
from starlette.responses import HTMLResponse

app = FastAPI()

# Параметры строки запроса представляют еще один способ передать в приложение некоторые значения в запросе типа GET.
# Для начала надо понимать, что такое строка запроса. Например, возьмем следующий адрес
# http://127.0.0.1:8000/users/add?name=Tom&age=38

# Если строка запроса содержит несколько параметров, то они одтеляются друг от друга знаком амперсанда &.
# Так, в примере в адресом http://127.0.0.1:8000/users/add?name=Tom&age=38
# строка запроса состоит из двух параметров: параметр name имеет значение "Tom", а параметр age имеет значение 38.

@app.get("/users", response_class=PlainTextResponse)
async def root_users(name, age):
    return f"User: {name}, age: {age}"

# Пример запуска http://127.0.0.1:8989/users?name=Tom&age=23


# Значения по умолчанию и с ограничениями
@app.get("/adduser", response_class=HTMLResponse)
async def root_add(name: str = "Noname", age: int = 0):
    return f"<h2> This is {name} and age = {age} </h2>"
# запуск http://127.0.0.1:8989/adduser?name=Daniil&age=78
# http://127.0.0.1:8989/adduser



# Query
# Дополнительно для работы с параметрами строки запроса фреймворк предоставляет класс Query из пакета fastapi. Класс Query позволяет прежде всего валидировать значения параметров строки запроса. В частности, через конструктор Query можно установить следующие параметры для валидации значений:
#
# min_length: устанавливает минимальное количество символов в значении параметра
#
# max_length: устанавливает максимальное количество символов в значении параметра
#
# pattern: устанавливает регулярное выражение, которому должно соответствовать значение параметра
#
# lt: значение параметра должно быть меньше определенного значения
#
# le: значение параметра должно быть меньше или равно определенному значению
#
# gt: значение параметра должно быть больше определенного значения
#
# ge: значение параметра должно быть больше или равно определенному значению

@app.get("/test_users")
async def users(name: str = Query(default="Undefined", min_length=2)):
    return {"name": name}

# http://127.0.0.1:8989/test_users?name=asdf
# http://127.0.0.1:8989/test_users


# Использование класса Query позволяет получать через строку запроса списки.
# В общем случае списки значений передаются, когда в строке запроса одному параметру несколько раз передаются разные значения.
# Например, как в запросе по следующему адресу:
# http://127.0.0.1:8000/users?people=tom&people=Sam&people=Bob
@app.get("/users_list")
async def list_users(names: list[str] = Query()):
    return {"names" : ", ".join(names)}

# запуск: http://127.0.0.1:8989/users_list?names=Tom&names=Daniil&names=kirill


# рассмотрим сочетание параметров пути и строки запроса
@app.get("/path_query/{name}", response_class=PlainTextResponse)
async def path_query(name: str = Path(min_length=3, max_length=16),
                     age: int = Query(gt=18, lt=111)):
    return f"name = {name}, age = {age}"

# запуск: http://127.0.0.1:8989/path_query/Tom?age=23
