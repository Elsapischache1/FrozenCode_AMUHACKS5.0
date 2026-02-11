from luna import get_luna_response

response = get_luna_response(
    user_message="How do I write a for loop in Python?",
    skill="Python",
    level="beginner"
)

print(response)
