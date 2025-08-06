from fastapi import FastAPI, Form
from fastapi.responses import FileResponse

app = FastAPI()

# в файле lesson5/logform.html создана простейшая форма для отправки данных. по post запросу /login отправляются данные
# из формы и получаем их в true_login.
@app.get("/login", response_class=FileResponse)
def login():
    return "lesson5/logform.html"

@app.post("/login")
def true_login(username = Form(), userage = Form()):
    return {"name" : username, "age" : userage}


