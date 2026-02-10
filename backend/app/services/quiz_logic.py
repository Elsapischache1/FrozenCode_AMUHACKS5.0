import google.generativeai as genai
import os

# ---------- CONFIG ----------
# Put your Gemini API key in an environment variable
# Windows (PowerShell):
# setx GEMINI_API_KEY "your_api_key_here"

API_KEY = "AIzaSyBuXr2IKLW-qQFfpkU2aYas__0U-36Fsts"

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-3-flash-preview")


# ---------- QUIZ LOGIC ----------
def generate_question(topic: str, difficulty: str = "easy") -> dict:
    prompt = f"""
    Create ONE {difficulty} level quiz question on the topic "{topic}".
    Return strictly in this format:

    Question: ...
    Option A: ...
    Option B: ...
    Option C: ...
    Option D: ...
    Correct Answer: A/B/C/D
    """

    response = model.generate_content(prompt)
    text = response.text.strip()

    lines = text.split("\n")
    data = {}

    for line in lines:
        if ":" in line:
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip()

    return {
        "question": data.get("Question"),
        "options": {
            "A": data.get("Option A"),
            "B": data.get("Option B"),
            "C": data.get("Option C"),
            "D": data.get("Option D"),
        },
        "answer": data.get("Correct Answer")
    }


def check_answer(user_answer: str, correct_answer: str) -> bool:
    return user_answer.upper() == correct_answer.upper()
