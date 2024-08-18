import json
import pandas as pd
from Agents.ReflexionAgent.graph.llm import llm
from Agents.ReflexionAgent.graph.chains.data_insight import insight_extraction_agent_prompt_template, AnswerQuestionInsight
from langchain_core.output_parsers.openai_tools import PydanticToolsParser


def data_visualization(scraped_file):
    with open(scraped_file, "r") as json_file:
        json_data = json.load(json_file)

    parser_pydantic = PydanticToolsParser(tools=[AnswerQuestionInsight])
    insights = insight_extraction_agent_prompt_template.partial(data = lambda:json_data, function_name=AnswerQuestionInsight.__name__,)
    data_insight_extractor = insights | llm.bind_tools(tools=[AnswerQuestionInsight]) | parser_pydantic
    result = data_insight_extractor.invoke(input={"messages": ["find key insights from this data in json format"]})
    print(result)
    # Extract JSON string from the `tool` field
    json_string = result[0].answer
    json_data = json.loads(json_string)
    with open("tools_results/insights.json", "w") as json_file:
        json.dump(json_data, json_file, indent=4)
    return json_string