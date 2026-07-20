from ddgs import DDGS


class Search:

    def search(self, query: str):

        with DDGS() as ddgs:

            results = list(
                ddgs.text(
                    query,
                    max_results=5
                )
            )

        return results