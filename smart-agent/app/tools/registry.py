from tools.search_tool import SearchTool


class ToolRegistry:

    def __init__(self):

        self.tools = {
            "search": SearchTool()
        }

    def get(self, name):

        return self.tools.get(name)

    def list_tools(self):

        return list(self.tools.keys())