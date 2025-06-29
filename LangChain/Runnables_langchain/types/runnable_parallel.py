from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel
load_dotenv()

llm1 = ChatGoogleGenerativeAI(model = 'gemini-2.0-flash')
llm2 = ChatGoogleGenerativeAI(model= 'gemma-3-27b-it')
prompt1 = PromptTemplate(
    template='Generate a short tweet about {topic}',
    input_variables=['topic']
)
prompt2 = PromptTemplate(
    template='Generate a short LinkedIn about {topic}',
    input_variables=['topic']
)
parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'tweet' : RunnableSequence(prompt1, llm2, parser),
    'LinkedIn' : RunnableSequence(prompt2, llm2, parser)
})

result = parallel_chain.invoke({'topic' : 'AI'})
print(result['tweet'], end='\n\n')
print(result['LinkedIn'])