from fastapi import FastAPI
from pydantic import BaseModel, Field, field_validator
import re


app = FastAPI()

feedbacks = []

FORBIDDEN_WORDS = ["редиска", "редиски", "редиске", "редиску", "редиской",
                  "бяка", "бяки", "бяке", "бяку", "бякой",
                  "козявка", "козявки", "козявке", "козявку", "козявкой"]

class Feedback(BaseModel):
    name : str = Field(min_length=2, max_length=50)
    message : str = Field(min_length=10, max_length=500)

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
def post_feedback(feedback: Feedback):
    feedbacks.append({"name" : feedback.name, "message" : feedback.message})
    return {"message" : f"Спасибо за отзыв {feedback.name}"}