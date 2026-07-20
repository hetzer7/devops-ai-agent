from ollama import chat


class LLM:

    def __init__(self, model="qwen3:8b"):

        self.model = model

    def ask(self, messages):

        response = chat(
            model=self.model,
            messages=messages
        )

        return response["message"]["content"]

    def ask_with_search(self, question, search_results):

        context = ""

        for item in search_results:

            context += f"""
제목:
{item["title"]}

내용:
{item["body"]}

링크:
{item["href"]}

-------------------------

"""

        prompt = f"""
당신은 친절한 AI Assistant입니다.

아래 검색 결과를 참고하여 답변하세요.

검색 결과

{context}

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

        return response["message"]["content"]