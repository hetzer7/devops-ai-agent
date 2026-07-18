from ollama import chat

response = chat(
    model="qwen3:8b",
    messages=[
        {
            "role": "user",
            "content": "안녕하세요"
        }
    ]
)

print(response["message"]["content"])
