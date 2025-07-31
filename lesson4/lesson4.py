from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI() # создаем приложение

@app.get("/")
async def root():
    return FileResponse("lesson4/index.html")

@app.get("/calculate")
async def root_calculate():
    return FileResponse("lesson4/calculate.html")

