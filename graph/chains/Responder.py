"""
This chain is for writing Initial responder which generate an initial response (and self-reflection)

This chain needs:
    1. Functions to Reflect and Answer
    2. Prompt Template and pipe it to LLM
"""

# load env variables
from dotenv import load_dotenv
from langchain_core.messages import BaseMessage, ToolMessage, AIMessage

load_dotenv()

from langchain_core.output_parsers.openai_tools import (
    JsonOutputToolsParser,  # This transform the output to JSON
    PydanticToolsParser  # This transform the output to Pydantic model
)
# MessagesPlaceholder: keep all the history
# ChatPromptTemplate: This will hold all our prompt content that we either send to the LLM
# as humans, or that we receive back from the LM as an answer that is tagged as an AI.
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from Agents.ReflexionAgent.graph.llm import llm

from typing import List
from langchain_core.pydantic_v1 import BaseModel, Field
import datetime
from Agents.ReflexionAgent.graph.prompts import response_instruction_system, response_instruction_user, response_first_instruction

# import tools' file name
from Agents.ReflexionAgent.graph.nodes.tools import tool_list

class AnswerQuestion(BaseModel):
    """Answer the question"""
    tool: str = Field(description="answer to the question")
    search_queries: List[str] = Field(
        description=
        """
        1-3 search queries based on what question is asking. 
        For example:
        collect some data about elon musk:
        Who is elon musk
        what elon musk did
        why elon musk is rich 
        """
    )

### Prompt Template and pipe it to LLM ###
actor_prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system",
        response_instruction_system,
         ),
        MessagesPlaceholder(variable_name="messages"),
        (
            "user",
            response_instruction_user,
        ),
    ]
    # This allows us to fill the variable in prompt. We put this here to run only when we invoke the Agent
).partial(time=lambda: datetime.datetime.now().isoformat(), tools=lambda: tool_list)

# Defining LLM

parser_json = JsonOutputToolsParser(return_id=True)
parser_pydantic = PydanticToolsParser(tools=[AnswerQuestion])

# Defining Chain
initial_answer_chain = (actor_prompt_template.partial(first_instruction= response_first_instruction, function_name=AnswerQuestion.__name__,)
                        | llm.bind_tools(tools=[AnswerQuestion])) | parser_pydantic





