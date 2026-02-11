import google.generativeai as genai
import json
import random

# ================= CONFIG =================
GEMINI_API_KEY = "AIzaSyDyjJL6SlxsuO7wxUiG_YZ2fCVO4cdbAhY4" 
MODEL_NAME = "gemini-3-flash-preview"

USE_CACHE = False  
QUESTION_CACHE = {}

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel(
    MODEL_NAME,
    generation_config={
        "temperature": 0.9
    }
)

def generate_questions_for_level(skill: str, level: str, count: int = 5):
    seed = random.randint(1, 1_000_000)
    cache_key = f"{skill}_{level}_{seed}"

    if USE_CACHE and cache_key in QUESTION_CACHE:
        return QUESTION_CACHE[cache_key]

    prompt = f"""
    Random seed: {seed}

    Generate {count} {level} level multiple choice questions on "{skill}".

    Rules:
    - Return ONLY valid JSON
    - Exactly 4 options per question
    - answer must be a NUMBER from 1 to 4
    - Do NOT include explanations or markdown

    Format:
    [
      {{
        "question": "...",
        "options": ["...", "...", "...", "..."],
        "answer": 1
      }}
    ]
    """

    response = model.generate_content(prompt)
    raw = response.text.strip()

    try:
        questions = json.loads(raw)
    except json.JSONDecodeError:
        # retry once with stricter instruction
        retry = model.generate_content(prompt + "\nREMEMBER: JSON ONLY.")
        questions = json.loads(retry.text.strip())

    if USE_CACHE:
        QUESTION_CACHE[cache_key] = questions

    return questions


class QuizEngine:
    def __init__(self, skill="Python"):
        self.questions = {
            "beginner": generate_questions_for_level(skill, "beginner"),
            "intermediate": generate_questions_for_level(skill, "intermediate"),
            "advanced": generate_questions_for_level(skill, "advanced"),
        }

        self.scores = {
            "beginner": 0,
            "intermediate": 0,
            "advanced": 0,
        }

        self.current_level = "beginner"
        self.current_index = 0

    def switch_level(self, level: str):
        if self.current_level != level:
            self.current_level = level
            self.current_index = 0

    def get_next_question(self):
        qs = self.questions[self.current_level]
        if self.current_index >= len(qs):
            return None
        return qs[self.current_index]

    def submit_answer(self, selected_option: int):
        """
        selected_option must be 1–4
        """
        q = self.questions[self.current_level][self.current_index]

        if selected_option == q["answer"]:
            self.scores[self.current_level] += 1

        self.current_index += 1

    def final_level(self):
        return min(self.scores, key=self.scores.get)


