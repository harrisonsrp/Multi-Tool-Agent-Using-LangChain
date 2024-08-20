from Agents.ReflexionAgent.graph.chains.Responder import initial_answer_chain
from Agents.ReflexionAgent.graph.nodes.tools  import execute_tools



if __name__ == "__main__":
    human_msg = "give me a table of information about this data"
    res = initial_answer_chain.invoke(input={"messages": [human_msg]})
    tool = execute_tools(res)
    print(tool)

