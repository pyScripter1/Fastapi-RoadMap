from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI()

feedbacks = {}

class FeedBack(BaseModel):
    name : str
    message : str

@app.get("/")
def root():
    return HTMLResponse("<h1>Feedbacks</h1>")

@app.get("/feedbacks")
def get_feedbacks():
    return feedbacks

@app.post("/feedback")
def post_feedback(feedback: FeedBack):
    feedbacks[feedback.name] = feedback.message
    return {"message": f"Feedback received. Thank you, {feedback.name}."}

