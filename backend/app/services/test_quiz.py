from quiz_logic import QuizEngine

engine = QuizEngine(skill="Python")

for level in ["beginner", "intermediate", "advance"]:
    print(f"\n===== {level.upper()} LEVEL =====")
    engine.switch_level(level)

    while True:
        q = engine.get_next_question()
        if q is None:
            break

        print("\nQ:", q["question"])
        for i, opt in enumerate(q["options"], start=1):
            print(f"{i}. {opt}")

        # dummy input for testing
        user_answer = int(input("Your answer (1-4): "))
        engine.submit_answer(user_answer)

print("\nFINAL SCORES:", engine.scores)
print("FINAL LEVEL:", engine.final_level())


