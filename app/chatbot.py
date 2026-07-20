from app.llm import LLM


class ChatBot:

    def __init__(self):

        self.messages = []
        self.llm = LLM()

    def ask(self, question):

        self.messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        answer = self.llm.ask(self.messages)

        self.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

        return answer