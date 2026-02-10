import os
import json
from openai import OpenAI

# Initialize OpenAI client (API key must be in env variable)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_questions_by_level(level: str):
    prompt = f"""
Generate EXACTLY 5 multiple-choice questions for Python at {level.upper()} level.

Rules:
- Each question must have 4 options
- Only ONE correct answer
- correct_answer must be an index (0-3)
- Return ONLY valid JSON
- No explanation, no markdown

Format:
[
  {{
    "question": "",
    "options": ["", "", "", ""],
    "correct_answer": 0,
    "level": "{level}"
  }}
]
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return json.loads(response.choices[0].message.content)


def generate_questions():
    return {
        "beginner": generate_questions_by_level("beginner"),
        "intermediate": generate_questions_by_level("intermediate"),
        "advanced": generate_questions_by_level("advanced")
    }


def evaluate_answers(user_answers, questions):
    scores = {
        "beginner": 0,
        "intermediate": 0,
        "advanced": 0
    }

    for level in questions:
        for i, q in enumerate(questions[level]):
            if user_answers[level][i] == q["correct_answer"]:
                scores[level] += 1

    if scores["advanced"] >= 3:
        final_level = "Advanced"
    elif scores["intermediate"] >= 3:
        final_level = "Intermediate"
    else:
        final_level = "Beginner"

    return {
        "scores": scores,
        "final_level": final_level
    }
