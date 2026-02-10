# luna.py
# Member 4: Chatbot logic

from pathlib import Path

BASE_PROMPT_PATH = Path(__file__).resolve().parent.parent / "prompts" / "luna_base.txt"

def load_base_prompt():
    with open(BASE_PROMPT_PATH, "r") as file:
        return file.read()

def get_luna_response(user_message, skill, level):
    base_prompt = load_base_prompt()

    full_prompt = f"""
{base_prompt}

User Skill: {skill}
User Level: {level}

User Question:
{user_message}
"""

    # TEMP response (LLM will replace this later)
    return {
        "reply": f"Luna received your question about {skill} at {level} level."
    }
