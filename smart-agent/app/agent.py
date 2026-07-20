from chatbot import ChatBot
from router import Router
from tools.registry import ToolRegistry


class Agent:

    def __init__(self):

        self.chatbot = ChatBot()

        self.registry = ToolRegistry()

        self.router = Router(self.registry)

    def ask(self, question):

        tool = self.router.route(question)

        if tool == "search":

            search = self.registry.get("search")

            results = search.execute(question)

            return self.chatbot.llm.ask_with_search(
                question,
                results
            )

        return self.chatbot.ask(question)