from quiz_logic import generate_question, check_answer

def run_test():
    quiz = generate_question(topic="Python", difficulty="easy")

    print("\nQUESTION:")
    print(quiz["question"])

    print("\nOPTIONS:")
    for key, value in quiz["options"].items():
        print(f"{key}. {value}")

    user_ans = input("\nYour answer (A/B/C/D): ").strip()

    if check_answer(user_ans, quiz["answer"]):
        print("✅ Correct!")
    else:
        print(f"❌ Wrong. Correct answer is {quiz['answer']}")

if __name__ == "__main__":
    run_test()
