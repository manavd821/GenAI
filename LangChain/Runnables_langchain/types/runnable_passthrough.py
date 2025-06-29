from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnablePassthrough, RunnableParallel
load_dotenv()

llm1 = ChatGoogleGenerativeAI(model = 'gemini-2.0-flash')
llm2 = ChatGoogleGenerativeAI(model= 'gemma-3-27b-it')

promp1 = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

parser = StrOutputParser()

first_chain = promp1 | llm1 | parser

prompt2 = PromptTemplate(
    template='Roast the joke based on its humor level in 2 lines.\nJoke: {joke}',
    input_variables=['joke']
)
parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'roast' :  prompt2 | llm2 | parser
})
final_chain = RunnableSequence(first_chain, parallel_chain)
result = final_chain.invoke({'topic' : 'AI'})
print('Joke: ', result['joke'])
print('roast:\n', result['roast'])
