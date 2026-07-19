class Planner:

    SEARCH_KEYWORDS = [
        "오늘",
        "최신",
        "뉴스",
        "날씨",
        "주가",
        "환율",
    ]

    def need_search(self, question: str) -> bool:

        for keyword in self.SEARCH_KEYWORDS:

            if keyword in question:
                return True

        return False