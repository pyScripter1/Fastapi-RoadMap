from fastapi import FastAPI


app = FastAPI()

fake_db = {
    1 : "Alex",
    2 : "Daniil",
    3 : "Ivan",
    4 : "Leha",
    5 : "Sasha"
}

@app.get("/users")
def get_users():
    return fake_db

@app.get("/users/{id}")
def get_user(id: int):
    if id in fake_db:
        return fake_db[id]
    return {"message" : "Error, not found"}



