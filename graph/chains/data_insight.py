from Agents.ReflexionAgent.graph.prompts import insight_instructions, response_instruction_user
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.pydantic_v1 import Field
from langchain_core.pydantic_v1 import BaseModel

class AnswerQuestionInsight(BaseModel):
    """Answer the question"""
    answer: str = Field(description="answer the question")



insight_extraction_agent_prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system",
    insight_instructions
         ),
        MessagesPlaceholder(variable_name="messages"),
        (
            "user",
            response_instruction_user,
        ),
    ]
)



