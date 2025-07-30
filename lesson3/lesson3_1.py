from fastapi import FastAPI, Path
from fastapi.responses import PlainTextResponse

app = FastAPI()

# рассмотрим подробно параметры пути
@app.get("/user/{name}/{id}", response_class=PlainTextResponse)
def users(name: str, id: int): # ограничения параметров пути
    return f"На страницу зашел пользователь {name}, id = {id}"


# можно использовать класс Path для доп работы с параметрами пути
@app.get("/test/{name}/{age}", response_class=PlainTextResponse)
def test(name: str = Path(min_length=3, max_length=16), age: int = Path(gt=18, lt=111)):
    return f"This is {name} and age is {age}"



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