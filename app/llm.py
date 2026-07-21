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

    ########################################################
    # 일반 대화
    ########################################################
    def ask(self, messages):

        start = time.time()

        response = self.client.chat(
            model=self.model,
            messages=messages
        )

        elapsed = time.time() - start

        print(f"[LLM] Time : {elapsed:.2f} sec")

        return response["message"]["content"]

    ########################################################
    # 검색 결과를 이용한 답변
    ########################################################
    def ask_with_search(self, question, search_results):

        context = ""

        # 검색 결과 최대 3개만 사용
        for item in search_results[:3]:

            title = item.get("title", "")
            body = item.get("body", "")[:300]
            href = item.get("href", "")

            context += f"""
제목: {title}

내용:
{body}

링크:
{href}

--------------------------
"""

        prompt = f"""
검색 결과를 참고하여 질문에 답변하세요.

{context}

질문:
{question}

답변:
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