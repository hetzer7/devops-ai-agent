import json

from ollama import chat


class Router:

    def __init__(self, registry, model="qwen3:8b"):

        self.registry = registry
        self.model = model

    def route(self, question):

        tools = self.registry.list_tools()

        tool_text = ", ".join(tools)

        prompt = f"""
당신은 AI Router입니다.

사용 가능한 Tool

{tool_text}

규칙

1. Tool이 필요하면 Tool 이름을 선택하세요.
2. Tool이 필요 없으면 chat을 선택하세요.
3. 반드시 JSON만 출력하세요.
4. 설명은 하지 마세요.

예시

{{"tool":"search"}}

{{"tool":"chat"}}

질문

{question}
"""

        response = chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        answer = response["message"]["content"].strip()

        print(f"[Router Raw] {answer}")

        try:

            result = json.loads(answer)

            return result["tool"]

        except Exception:

            return "chat"