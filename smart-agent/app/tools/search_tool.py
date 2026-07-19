from ddgs import DDGS


class SearchTool:

    def execute(self, question):

        print("[SearchTool] 인터넷 검색")

        with DDGS() as ddgs:

            results = list(
                ddgs.text(
                    question,
                    max_results=5
                )
            )

        return results