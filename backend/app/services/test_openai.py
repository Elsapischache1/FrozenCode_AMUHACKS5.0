import os
import requests
import json

API_KEY = os.getenv("GEMINI_API_KEY")

url = (
    "https://generativelanguage.googleapis.com/v1beta/models/"
    "gemini-1.0-pro:generateContent?key=" + API_KEY
)

payload = {
    "contents": [
        {
            "parts": [
                {"text": "Say hello"}
            ]
        }
    ]
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, headers=headers, data=json.dumps(payload))
data = response.json()

print("FULL RESPONSE:")
print(json.dumps(data, indent=2))

if "candidates" in data:
    print("\nMODEL OUTPUT:")
    print(data["candidates"][0]["content"]["parts"][0]["text"])
else:
    print("\nERROR FROM GOOGLE:")
    print(data)


