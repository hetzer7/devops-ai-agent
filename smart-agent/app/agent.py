from chatbot import ChatBot
from router import Router
from tools.registry import ToolRegistry


class Agent:

    def __init__(self):

        self.chatbot = ChatBot()

        self.registry = ToolRegistry()

        self.router = Router(self.registry)

    def ask(self, question):

        tool_name = self.router.route(question)

        if tool_name == "chat":

            return self.chatbot.ask(question)

        tool = self.registry.get(tool_name)

        if tool is None:

            return "알 수 없는 Tool입니다."

        result = tool.execute(question)

        if result["type"] == "search":

            return self.chatbot.llm.ask_with_search(
                question,
                result["data"]
            )

        return "아직 처리할 수 없는 Tool입니다."