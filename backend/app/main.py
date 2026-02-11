from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Import your services
from app.services.quiz_logic import QuizEngine
from app.services.luna import get_luna_response

app = FastAPI(title="Synapse Backend")

# CORS middleware - allows React to communicate with FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global State
quiz_engine: QuizEngine | None = None

class StartQuizRequest(BaseModel):
    skill: str

class AnswerRequest(BaseModel):
    level: str
    selected_option: int

class LunaRequest(BaseModel):
    user_message: str
    skill: str
    level: str

@app.get("/")
def read_root():
    return {"message": "Synapse Backend is running!"}

@app.post("/quiz/start")
def start_quiz(data: StartQuizRequest):
    global quiz_engine
    print(f"✅ Starting quiz for: {data.skill}")
    quiz_engine = QuizEngine(skill=data.skill)
    return {"message": "Quiz started", "skill": data.skill}

@app.get("/quiz/question/{level}")
def get_question(level: str):
    if quiz_engine is None:
        return {"error": "Quiz not started"}
    
    if quiz_engine.current_level != level:
         quiz_engine.switch_level(level)

    q = quiz_engine.get_next_question()
    if q is None:
        return {"done": True}
    return q

@app.post("/quiz/answer")
def submit_answer(data: AnswerRequest):
    if quiz_engine:
        quiz_engine.submit_answer(data.selected_option)
        return {"status": "answer recorded"}
    return {"status": "error", "message": "No active quiz"}

@app.get("/quiz/result")
def quiz_result():
    if quiz_engine:
        return {
            "scores": quiz_engine.scores,
            "final_level": quiz_engine.final_level()
        }
    return {"error": "No result available"}

@app.post("/luna/chat")
def luna_chat(data: LunaRequest):
    response = get_luna_response(
        user_message=data.user_message,
        skill=data.skill,
        level=data.level
    )
    return {"response": response}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)