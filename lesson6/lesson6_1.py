# Pydantic-модели для аннотации типов в FastAPI
# Pydantic — это Python-библиотека для выполнения валидации данных.
#
# Вы объявляете «форму» данных как классы с атрибутами, и каждый атрибут имеет тип.
# Затем вы создаёте экземпляр этого класса с некоторыми значениями, и Pydantic проверяет эти значения,
# преобразует их в соответствующий тип (если данные корректны) и предоставляет вам объект со всеми данными.

# Пример создания модели
# вставьте этот код в любой файл, который бы вы могли выполнить
# например это abc.py, который вы запустите в терминале командой python3 abc.py
from datetime import datetime
from pydantic import BaseModel

# Создаём модель данных, которая обычно располагается в файле models.py
class User(BaseModel):
    id: int
    name: str = "John Doe"
    signup_ts: datetime | None = None
    friends: list[int] = []

# Внешние данные, имитирующие входящий JSON
external_data = {
    "id": "123",
    "signup_ts": "2017-06-01 12:22",
    "friends": [1, "2", b"3"],
}

# Имитация распаковки входящих данных в коде приложения
user = User(**external_data)
print(user)
# > User id=123 name='John Doe' signup_ts=datetime.datetime(2017, 6, 1, 12, 22) friends=[1, 2, 3]
print(user.id)
# > 123

# В этом примере Pydantic автоматически преобразует строку "123" в целое число,
# дату в объект datetime, а элементы списка, такие как "2" или b"3", в целые числа.


# Пример реального post запроса с использование pydantic модели
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    username: str
    message: str


@app.post("/")
async def root(user: User):
    """
    Здесь мы можем с переменной user, которая содержит объект класса User с соответствующими полями,
    выполнить любую логику – например, сохранить информацию в базу данных, передать в другую функцию и т.д.
    """
    print(f'Мы получили от юзера {user.username} такое сообщение: {user.message}')
    return user