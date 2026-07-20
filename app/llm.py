import os
import time


from ollama import Client


class LLM:

    def __init__(self, model="qwen3:8b"):

        self.model = model

        ollama_host = os.getenv(
            "OLLAMA_BASE_URL",
            "http://localhost:11434"
        )

        print(f"[LLM] Ollama Host : {ollama_host}")

        self.client = Client(host=ollama_host)

    def ask(self, messages):

        start = time.time()

        response = self.client.chat(
            model=self.model,
            messages=messages
        )

        elapsed = time.time() - start

        print(f"[LLM] Time : {elapsed:.2f} sec")

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

        start = time.time()

        response = self.client.chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        elapsed = time.time() - start

        print(f"[LLM Search] Time : {elapsed:.2f} sec")

        return response["message"]["content"]