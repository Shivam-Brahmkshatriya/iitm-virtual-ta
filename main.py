from fastapi import FastAPI, Request
from pydantic import BaseModel
import json
from utils import find_best_match

app = FastAPI()

# Load data
with open("data.json", "r") as f:
    data = json.load(f)

class QuestionInput(BaseModel):
    question: str
    image: str = None

@app.post("/api/")
def answer_question(input: QuestionInput):
    question = input.question
    match = find_best_match(question, data)
    return {
        "answer": f"Based on similar discussions, check this post: {match['title']}",
        "links": [{"url": match["url"], "text": match["title"]}]
    }
