from fastapi import FastAPI
from pydantic import BaseModel

from app.services.quiz_logic import QuizEngine
from app.services.luna import get_luna_response

app = FastAPI(title="Synapse Backend")

quiz_engine: QuizEngine | None = None

class StartQuizRequest(BaseModel):
    skill: str

class AnswerRequest(BaseModel):
    level: str
    selected_option: int  # 1–4

class LunaRequest(BaseModel):
    user_message: str
    skill: str
    level: str

@app.post("/quiz/start")
def start_quiz(data: StartQuizRequest):
    global quiz_engine
    quiz_engine = QuizEngine(skill=data.skill)
    return {"message": "Quiz started", "skill": data.skill}

@app.get("/quiz/question/{level}")
def get_question(level: str):
    if quiz_engine.current_level != level:
         quiz_engine.switch_level(level)

    q = quiz_engine.get_next_question()
    if q is None:
        return {"done": True}
    return q

@app.post("/quiz/answer")
def submit_answer(data: AnswerRequest):
    quiz_engine.submit_answer(data.selected_option)
    return {"status": "answer recorded"}

@app.get("/quiz/result")
def quiz_result():
    return {
        "scores": quiz_engine.scores,
        "final_level": quiz_engine.final_level()
    }

@app.post("/luna/chat")
def luna_chat(data: LunaRequest):
    response = get_luna_response(
        user_message=data.user_message,
        skill=data.skill,
        level=data.level
    )
    return {"response": response}
