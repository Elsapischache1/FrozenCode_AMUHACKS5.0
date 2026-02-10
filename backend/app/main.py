from fastapi import FastAPI
from app.services.quiz_logic import generate_questions, evaluate_answers

app = FastAPI()

@app.get("/test-quiz")
def test_quiz():
    questions = generate_questions()
    return questions

@app.post("/submit-quiz")
def submit_quiz(user_answers: dict):
    questions = generate_questions()
    result = evaluate_answers(user_answers, questions)
    return result
