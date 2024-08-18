from langgraph.prebuilt import ToolInvocation, ToolExecutor
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_community.utilities.tavily_search import TavilySearchAPIWrapper
from collections import defaultdict
from langchain_core.messages import ToolMessage
import json
import pandas as pd
from tabulate import tabulate
# Initialize the Tavily search tool with a maximum result limit of 3
search = TavilySearchAPIWrapper()
tavily_tool = TavilySearchResults(api_wrapper=search, max_result=1)
tool_executor = ToolExecutor([tavily_tool])

def url_search(search_queries):
    print("===== Starting URL search =====")
    tool_invocations = []  # List to store ToolInvocation objects
    for search_query in search_queries:
        print(search_query)
        tool_invocations.append(ToolInvocation(
            tool="tavily_search_results_json",  # Specify the tool to use
            tool_input=search_query  # Provide the query as input to the tool
        ))

    # Executes the collected tool invocations in a batch and retrieves the results
    outputs = tool_executor.batch(tool_invocations)
    outputs_map = defaultdict(dict)
    for output, invocation in zip(outputs, tool_invocations):
        outputs_map[invocation.tool_input] = output
    data = []
    for search_item,output in outputs_map.items():
            for i in output:
                data.append(i)

    # Create a DataFrame from the list of dictionaries
    df = pd.DataFrame(data)
    df.to_csv("tools_results/tavily_url_search_result.csv", index=False)

    urls = []
    for i in df['url']:
        urls.append(i)
    print("===== URL search complete =====")
    return urls