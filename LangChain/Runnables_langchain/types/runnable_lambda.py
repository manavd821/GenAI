from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnablePassthrough, RunnableParallel, RunnableLambda
load_dotenv()

llm1 = ChatGoogleGenerativeAI(model = 'gemini-2.0-flash')
llm2 = ChatGoogleGenerativeAI(model= 'gemma-3-27b-it')
llm3 = ChatGoogleGenerativeAI(model='learnlm-2.0-flash-experimental')

promp1 = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)
parser = StrOutputParser()
joke_generator = promp1 | llm3 | parser
parallel_chain = RunnableParallel({
    'joke' : RunnablePassthrough(),
    'count' : RunnableLambda(lambda x: len(x.strip().replace('\n','').split()))
})
# final_chain = joke_generator | parallel_chain
# result = final_chain.invoke({'topic' : 'AI'})
# print(result)
# print('Joke: ',result['joke'])
# print('Word Count: ',result['count'])

# another example
runnable = RunnableLambda(lambda x : x+1)
print(runnable.invoke(1))