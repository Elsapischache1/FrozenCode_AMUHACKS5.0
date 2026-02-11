import google.generativeai as genai
from pathlib import Path
import os

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "YOUR_API_KEY_HERE")
genai.configure(api_key=GEMINI_API_KEY)

BASE_PROMPT_PATH = Path(__file__).resolve().parent.parent.parent / "prompts" / "luna_base.txt"

with open( BASE_PROMPT_PATH,"r", encoding="utf-8") as f:
    SYSTEM_PROMPT = f.read()

model = genai.GenerativeModel(
    model_name="gemini-3-flash-preview",
    system_instruction=SYSTEM_PROMPT
)

def get_luna_response(user_message: str, skill: str, level: str) -> str:
    prompt = f"""
    Skill: {skill}
    User level: {level}

    User question:
    {user_message}

    Answer clearly and concisely, suitable for the given level.
    """

    response = model.generate_content(prompt)
    return response.text.strip()

