from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnablePassthrough, RunnableParallel, RunnableBranch, RunnableLambda
load_dotenv()

llm1 = ChatGoogleGenerativeAI(model = 'gemini-2.0-flash')
llm2 = ChatGoogleGenerativeAI(model= 'gemma-3-27b-it')
llm3 = ChatGoogleGenerativeAI(model='learnlm-2.0-flash-experimental')

# propmt1 = PromptTemplate(
#     template='Write a detail report on {topic}',
#     input_variables=['topic']
# )
# propmt2 = PromptTemplate(
#     template='Summarize the following text.\n{text}',
#     input_variables=['text']
# )
# parser = StrOutputParser()
# report_generation_chain = RunnableSequence(propmt1, llm3, parser)
# branch_chain = RunnableBranch(
#     (lambda x: len(x.strip().replace('\n','').split()) > 200 , RunnableSequence(propmt2, llm1, parser)),
#     # below default
#     RunnablePassthrough()
# )
# final_chain = RunnableSequence(report_generation_chain, branch_chain)
# print(final_chain.invoke({'topic' : 'Russia Vs Ukraine'}))

# Another Example
from pydantic import BaseModel, Field
from typing import Literal
from langchain_core.output_parsers import PydanticOutputParser
class Feedback(BaseModel):
    sentiment : Literal['positive', 'negative', 'neutral'] = Field(description='Give feedback either positive or negative or neutral')

feedback_generation_prompt = PromptTemplate(
    template='Generate a random {flavour} feedback about {product} in few lines.',
    input_variables=['product', 'flavour'],
)
feedback_generation_chain = feedback_generation_prompt | llm1 | StrOutputParser()

# print(feedback_generation_chain.invoke({'product' : 'Headphone'}))
parser = PydanticOutputParser(pydantic_object=Feedback)

feedback_review_prompt = PromptTemplate(
    template='Categories given feedback given formate.\nformate : {formate_instruction}\nFeedback: \n{feedback}',
    input_variables=['feedback'],
    partial_variables={'formate_instruction' : parser.get_format_instructions()}
)

feedback_review_chain = feedback_generation_chain | feedback_review_prompt | llm3 | parser
# result = feedback_review_chain.invoke({'product' : 'Headphone'})
# print(result.sentiment)
final_chain = feedback_review_chain | RunnableBranch(
    (lambda x: x.sentiment == 'positive', RunnableLambda(lambda _: {}) | PromptTemplate(
        template='What is capital of India? Write only one word answer.',
        input_variables=[]
    ) | llm2 | StrOutputParser()),
    (lambda x: x.sentiment == 'negative', RunnableLambda(lambda _: {}) | PromptTemplate(
        template='Explain array in one line',
        input_variables=[]
    ) | llm2 | StrOutputParser()),
    lambda x: RunnableLambda(lambda _: "Hare Krsna")
)

print(final_chain.invoke({'product' : 'Headphone', 'flavour' : 'positive'}))

## Another example
# branch = RunnableBranch(
#                 (lambda x: isinstance(x, str), lambda x: x.upper()),
#                 (lambda x: isinstance(x, int), lambda x: x + 1),
#                 (lambda x: isinstance(x, float), lambda x: x * 2),
#                 lambda x: "goodbye",
#             )

# print(branch.invoke("hello") )# "HELLO"
# print(branch.invoke(None)) # "goodbye"

