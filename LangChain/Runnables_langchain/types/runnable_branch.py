from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnablePassthrough, RunnableParallel, RunnableBranch
load_dotenv()

llm1 = ChatGoogleGenerativeAI(model = 'gemini-2.0-flash')
llm2 = ChatGoogleGenerativeAI(model= 'gemma-3-27b-it')
llm3 = ChatGoogleGenerativeAI(model='learnlm-2.0-flash-experimental')

propmt1 = PromptTemplate(
    template='Write a detail report on {topic}',
    input_variables=['topic']
)
propmt2 = PromptTemplate(
    template='Summarize the following text.\n{text}',
    input_variables=['text']
)
parser = StrOutputParser()
report_generation_chain = RunnableSequence(propmt1, llm3, parser)
branch_chain = RunnableBranch(
    (lambda x: len(x.strip().replace('\n','').split()) > 200 , RunnableSequence(propmt2, llm1, parser)),
    # below default
    RunnablePassthrough()
)
final_chain = RunnableSequence(report_generation_chain, branch_chain)
print(final_chain.invoke({'topic' : 'Russia Vs Ukraine'}))