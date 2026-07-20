from ddgs import DDGS

from tools.base_tool import BaseTool


class SearchTool(BaseTool):

    @property
    def name(self):
        return "search"

    def execute(self, question):

        print("[SearchTool] 인터넷 검색")

        with DDGS() as ddgs:

            results = list(
                ddgs.text(
                    question,
                    max_results=5
                )
            )

        return {
            "type": "search",
            "data": results
        }