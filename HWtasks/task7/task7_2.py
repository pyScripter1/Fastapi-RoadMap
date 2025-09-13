from typing import Annotated
import re
import datetime

from fastapi import FastAPI, Header, Query, HTTPException
from pydantic import BaseModel, field_validator


MINIMUM_APP_VERSION = "0.0.2"

app = FastAPI()

def validate_version(client_version: str, server_version: str) -> bool:
    client_version = map(int, client_version.split('.'))
    server_version = map(int, server_version.split('.'))
    result = zip(client_version, server_version)
    for common, server in result:
        if common > server:
            return True
        elif common < server:
            return False
    else:
        return True


class CommonHeaders(BaseModel):
    user_agent: str
    accept_language: str
    x_current_version: Annotated[str, Query(..., regex=r"^\d+\.\d+\.\d+$", example=MINIMUM_APP_VERSION)]

    @field_validator('accept_language')
    @classmethod
    def validate_accept_language(cls, lang: str) -> str:
        pattern = r"^([a-z]{1,8}(-[A-Z]{1,8})?|\*)(,\s*([a-z]{1,8}(-[A-Z]{1,8})?|\*)(;\s*q=[0-9.]+)?)*$"
        if not re.fullmatch(pattern, lang):
            raise HTTPException(400, detail="Invalid Accept-Language header")
        return lang

    def get_headers(self) -> dict:
        headers = {"User-Agent": self.user_agent,
                   "Accept-Language": self.accept_language,
                   "X-Server-Time": datetime.now(timezone.utc).replace(microsecond=0).isoformat()}
        return headers

    @field_validator('x_current_version')
    @classmethod
    def validate_current_version(cls, version: str) -> str:
        check_version = validate_version(version, MINIMUM_APP_VERSION)
        if not check_version:
            raise ValueError("The application needs to be updated")
        return version


@app.get("/headers")
async def get_headers(headers: Annotated[CommonHeaders, Header()]):
    headers: dict = headers.get_headers()
    return headers


@app.get("/info")
async def get_headers(headers: Annotated[CommonHeaders, Header()]):
    headers: dict = headers.get_headers()
    return {"message": "Добро пожаловать! Ваши заголовки успешно обработаны.",
            "headers": headers}
