from Agents.ReflexionAgent.graph.chains.Responder import initial_answer_chain
from Agents.ReflexionAgent.graph.nodes.tools  import execute_tools
# if __name__ == "__main__":
#     human_msg = "collect data of housing price in Montreal in the 2024"
#     res = initial_answer_chain.invoke(input={"messages": [human_msg]})
#     tool = execute_tools(res)
#     print(tool)

if __name__ == "__main__":
    human_msg = "make a table of key information from this data"
    res = initial_answer_chain.invoke(input={"messages": [human_msg]})
    tool = execute_tools(res)
    print(tool)