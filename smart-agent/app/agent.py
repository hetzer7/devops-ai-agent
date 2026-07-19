from chatbot import ChatBot
from planner import Planner
from tools.search_tool import SearchTool


class Agent:

    def __init__(self):

        self.chatbot = ChatBot()
        self.planner = Planner()
        self.search_tool = SearchTool()

    def ask(self, question):

        if self.planner.need_search(question):

            print("[Planner] Search Required")

            results = self.search_tool.execute(question)

            return self.chatbot.llm.ask_with_search(
                question,
                results
            )

        print("[Planner] Search Not Required")

        return self.chatbot.ask(question)