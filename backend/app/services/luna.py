import google.generativeai as genai
from pathlib import Path

GEMINI_API_KEY = "AIzaSyA5GCZy5au8m-pRfX95frrY0EEQpQW5V84"
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

