from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal
load_dotenv()

llm1 = ChatGoogleGenerativeAI(model = 'gemini-2.0-flash')
llm2 = ChatGoogleGenerativeAI(model= 'gemma-3-27b-it')

from langchain_core.output_parsers import StrOutputParser
parser = StrOutputParser()

class Feedback(BaseModel):
    sentiment : Literal['positive', 'negative'] = Field(description='Give the sentiment of the feedback')
    feedback : str = Field(description='user feedback')

parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template='Classify the sentiment of the following feedback into positive or negative.\n{feedback}\n{format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction':parser2.get_format_instructions()}
)


classifier_chain = prompt1 | llm1 | parser2
# result1 = classifier_chain.invoke({'feedback' : 'This is a wonderful smartphone'})
# print(type(result1))
# print(result1)

from langchain.schema.runnable import  RunnableBranch, RunnableLambda

# for positive feedback
prompt2 = PromptTemplate(
    template='Write an appropriate response to this positive feedback in short\n{feedback}',
    input_variables=['feedback']
)
# for negative feedback
prompt3 = PromptTemplate(
    template='Write an appropriate response to this negative feedback in short\n{feedback}',
    input_variables=['feedback']
)
branch_chain = RunnableBranch(
    # syntax : 
    # (condition1, chain2)
    # (condition2, chain3)
    # default chain
    (lambda x: x.sentiment == 'positive', prompt2 | llm2 | parser),
    (lambda x: x.sentiment == 'negative', prompt3 | llm2 | parser),
    RunnableLambda(lambda x: "could not find sentiment")
)

final_chain = classifier_chain | branch_chain
final_result =final_chain.invoke({'feedback': 'This is a wonderful phone'})
print(final_result)

final_chain.get_graph().print_ascii()