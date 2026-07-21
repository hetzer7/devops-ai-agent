class Router:

    def __init__(self, registry):

        self.registry = registry

        self.search_keywords = [

            "날씨",
            "뉴스",
            "검색",
            "최신",
            "현재",
            "실시간",
            "환율",
            "주가",
            "가격",
            "언제",
            "누구",
            "어디",
            "무엇",
            "왜",
            "어떻게"

        ]

    def route(self, question):

        question = question.lower()

        for keyword in self.search_keywords:

            if keyword in question:

                print(f"[Router] Rule -> search ({keyword})")

                return "search"

        print("[Router] Rule -> chat")

        return "chat"