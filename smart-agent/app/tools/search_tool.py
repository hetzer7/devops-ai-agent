from ddgs import DDGS


class SearchTool:

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