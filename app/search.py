from ddgs import DDGS


class Search:

    def search(self, query: str):

        with DDGS() as ddgs:

            results = list(
                ddgs.text(
                    query,
                    max_results=3
                )
            )

        return results