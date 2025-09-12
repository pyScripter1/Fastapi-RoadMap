import datetime
from typing import Annotated

from fastapi import FastAPI, Header, Response
from pydantic import BaseModel

app = FastAPI()

class CommonHeaders(BaseModel):
    user_agent : str
    accept_language : str

def format_headers(user_agent, accept_language):
    return {'User-Agent': user_agent,
            'Accept-Language': accept_language}

@app.get("/headers")
def get_headers(headers : Annotated[CommonHeaders, Header()]):
    return format_headers(headers.user_agent, headers.accept_language)

@app.get("/info")
def get_info(headers : Annotated[CommonHeaders, Header()], response : Response):
    response.headers["X-Server-Time"] = str(datetime.datetime.now())
    return {
        "message" : "Добро пожаловать! Ваши заголовки успешно обработано!",
        "headers" : format_headers(headers.user_agent, headers.accept_language)
    }