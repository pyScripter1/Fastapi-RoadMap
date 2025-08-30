from fastapi import FastAPI
from pydantic import BaseModel, Field, field_validator, EmailStr
from typing import Optional
import re


app = FastAPI()

feedbacks = []

FORBIDDEN_WORDS = ["редиска", "редиски", "редиске", "редиску", "редиской",
                  "бяка", "бяки", "бяке", "бяку", "бякой",
                  "козявка", "козявки", "козявке", "козявку", "козявкой"]

class Contact(BaseModel):
    email : EmailStr
    phone : Optional[str] = None

    @field_validator("phone")
    def check_phone(cls, phone):
        pattern = r"^\d{7,15}$"
        if phone is None:
            return
        if re.fullmatch(pattern, phone):
            return phone
        raise ValueError("Неверный номер телефона")

class Feedback(BaseModel):
    name : str = Field(min_length=2, max_length=50)
    message : str = Field(min_length=10, max_length=500)
    contact : Contact

    @field_validator("message")
    def check_message(cls, v):
        message_lower = v.lower()

        for bad_word in FORBIDDEN_WORDS:
            if bad_word in message_lower:
                raise ValueError("Использование недопустимых слов!")
            return v


@app.get("/feedbacks")
def get_feedbacks():
    return feedbacks

@app.post("/feedback")
def post_feedback(feedback: Feedback, is_premium: bool = False):
    feedbacks.append(
        {
            "name" : feedback.name,
            "message" : feedback.message,
            "contact" : {
                          "email" : feedback.contact.email,
                          "phone" : feedback.contact.phone
                        }
        }
    )
    if is_premium:
        return {"message" : f"Спасибо за отзыв {feedback.name}. Ваш отзыв будет рассмотрен в приоритетном порядке."}
    return {"message" : f"Спасибо за отзыв {feedback.name}."}