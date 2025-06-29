from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence
load_dotenv()

llm1 = ChatGoogleGenerativeAI(model = 'gemini-2.0-flash')
llm2 = ChatGoogleGenerativeAI(model= 'gemma-3-27b-it')
prompt = PromptTemplate(
    template='Write a joke on {topic}',
    input_variables=['topic']
)
parser = StrOutputParser()
prompt2 = PromptTemplate(
    template='Roast the joke based on its humor level.\nJoke: {joke}',
    input_variables=['joke']
)
# chain = prompt | llm2 | parser | prompt2 | llm1 | parser
chain = RunnableSequence(prompt, llm2, parser, prompt2, llm1, parser)
res = chain.invoke({'topic': 'AI'})
print(res)