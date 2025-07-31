from fastapi import FastAPI, Path, Response

app = FastAPI()

# изменение статусного кода
@app.get("/user/{id}", status_code=200)
async def user(response: Response, id: int = Path()):
    if id <= 0:
        response.status_code = 400
        return {"message" : "Incorrect Data"}
    return {"user" : id}

# В данном случае если параметр пути меньше 1,
# то условно считаем, что переданные некорректные данные, и отправляем в ответ статусный код 400 (Bad Request)

