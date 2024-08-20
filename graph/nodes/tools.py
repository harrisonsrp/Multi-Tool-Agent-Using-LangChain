from langchain_core.messages import BaseMessage, ToolMessage, AIMessage
from typing import List
from pathlib import Path
import json
# Adding tools
from Agents.ReflexionAgent.graph.tools.web_scraping import web_scraping
from Agents.ReflexionAgent.graph.tools.tavily import url_search
from Agents.ReflexionAgent.graph.tools.data_visualization import data_visualization

# tools directory path
directory = Path(r'C:\Projects\Agents\ReflexionAgent\graph\tools')

# list of tools in the directory
tool_list = [tool.name for tool in directory.iterdir()
             if tool.is_file() and tool.name != '__init__.py' and tool.name != 'tavily.py']


def execute_tools(state: [BaseMessage]) -> List[ToolMessage]:

    tool_invocation = state[-1]
    tool_name = tool_invocation.tool
    search_query = tool_invocation.search_queries
    if tool_name == 'web_scraping.py':
        print("==== Using Web Scraping Tool ====")
        search_for_url = url_search(search_query)
        web_scraping_data = web_scraping(search_for_url)
        return web_scraping_data
    if tool_name == 'data_visualization.py':
        print("==== Using Data Visualization Tool ====")
        json_file = "tools_results/scraped_data.json"
        data_visu = data_visualization(json_file)
        return data_visu
