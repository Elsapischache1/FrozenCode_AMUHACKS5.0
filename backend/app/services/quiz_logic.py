# quiz_logic.py
# Member 2: Question generation + evaluation logic

def generate_questions():
    """
    Returns questions grouped by difficulty.
    This is the structure the backend will consume.
    """

    questions = {
        "beginner": [
            {
                "question": "What does len() do in Python?",
                "options": [
                    "Counts number of items",
                    "Adds items",
                    "Deletes items",
                    "Sorts items"
                ],
                "correct_answer": 0,
                "level": "beginner"
            }
        ],
        "intermediate": [
            {
                "question": "What is the output of: print(type([]))?",
                "options": [
                    "<class 'list'>",
                    "<class 'dict'>",
                    "<class 'tuple'>",
                    "<class 'set'>"
                ],
                "correct_answer": 0,
                "level": "intermediate"
            }
        ],
        "advanced": [
            {
                "question": "Which of the following improves Python code performance?",
                "options": [
                    "Using global variables",
                    "Using list comprehensions",
                    "Using more loops",
                    "Using recursion everywhere"
                ],
                "correct_answer": 1,
                "level": "advanced"
            }
        ]
    }

    return questions


def evaluate_answers(user_answers, questions):
    """
    user_answers: dict with keys beginner/intermediate/advanced
    questions: output from generate_questions()
    """

    scores = {
        "beginner": 0,
        "intermediate": 0,
        "advanced": 0
    }

    for level in questions:
        for i, q in enumerate(questions[level]):
            if user_answers[level][i] == q["correct_answer"]:
                scores[level] += 1

    # Simple rule-based final level
    if scores["beginner"] >= 1 and scores["intermediate"] == 0:
        final_level = "Beginner"
    elif scores["intermediate"] >= 1 and scores["advanced"] == 0:
        final_level = "Intermediate"
    elif scores["advanced"] >= 1:
        final_level = "Advanced"
    else:
        final_level = "Beginner"

    return {
        "scores": scores,
        "final_level": final_level
    }
