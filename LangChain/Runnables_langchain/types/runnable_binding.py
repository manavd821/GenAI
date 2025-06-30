from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnablePassthrough, RunnableParallel, RunnableLambda, RunnableBinding
load_dotenv()

llm1 = ChatGoogleGenerativeAI(model = 'gemini-2.0-flash')
llm2 = ChatGoogleGenerativeAI(model= 'gemma-3-27b-it')

prompt =  PromptTemplate(
    template='Write about {topic} research paper from {way} perspective in few lines',
    input_variables=['topic','way']
) 



# runnable_binding = (PromptTemplate(template='{greet}\n. return above text as it is.', input_variables=['greet']) | llm1.bind(stop = [','])) | StrOutputParser()
# print(runnable_binding.invoke({'greet' : 'Hare Krsna, Manav'}))