from luna import get_luna_response

response = get_luna_response(
    user_message="What is a variable?",
    skill="Python",
    level="beginner"
)

print(response)
