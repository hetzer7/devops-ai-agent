from app.tools.search_tool import SearchTool


class ToolRegistry:

    def __init__(self):

        self.tools = {}

        self.register(SearchTool())

    def register(self, tool):

        self.tools[tool.name] = tool

    def get(self, name):

        return self.tools.get(name)

    def list_tools(self):

        return list(self.tools.keys())