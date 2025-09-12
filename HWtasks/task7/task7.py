"""
Ваша задача - создать приложение FastAPI, которое демонстрирует, как работать с заголовками запросов. Выполните следующие действия, чтобы выполнить задачу:

1. Создайте конечную точку в `/headers`, которая принимает запросы GET.

2. В конечной точке `/headers` извлеките следующие заголовки из входящего запроса:

   a) "User-agent": строка пользовательского агента браузера клиента или пользовательского агента пользователя.

   б) "Accept-Language": предпочтительный язык клиента для согласования содержимого.

3. Верните ответ в формате JSON, содержащий извлеченные заголовки и их значения.

4. Реализуйте обработку (выбрасывание) ошибок, чтобы вернуть соответствующий ответ с кодом состояния 400 (неверный запрос), если необходимые заголовки отсутствуют.

5. Необязательно: добавьте проверку, чтобы проверить, имеет ли заголовок "Accept-Language" правильный формат (например, "en-US,en;q=0.9,es;q=0.8"). Если он не в правильном формате, верните ответ об ошибке с кодом состояния 400 (неверный запрос).

Подсказка: Используйте атрибут `request.headers` или прямое указание на класс `Header` для доступа к заголовкам входящих запросов.
"""
from typing import Annotated

from fastapi import FastAPI, Header, HTTPException


app = FastAPI()

@app.get("/headers")
def root(user_agent : Annotated[str | None, Header()] = None,
         accept_language : Annotated[str | None, Header()] = None):
    if user_agent is None :
        raise HTTPException(status_code=400, detail="Must be user-agent and accept-language")
    # if accept_language != "en-US,en;q=0.9,es;q=0.8":
    #     raise HTTPException(status_code=400, detail="Accept-Language is bad format")
    return {
        "User-Agent" : user_agent,
        "Accept-Language" : accept_language
    }
