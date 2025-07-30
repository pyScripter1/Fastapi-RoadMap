# импортируем класс Fastapi для создания приложения
from fastapi import FastAPI

app = FastAPI()

@app.get("/") # один из базовых запросов
async def root():
    return {"message" : "hello world"}

# для запуска uvicorn lesson1.lesson1:app --reload (так как файд lesson1.py находится в директории lesson1
# для запуска uvicorn lesson1.lesson1:app --reload --port 8080 (если порт 8000 занят)