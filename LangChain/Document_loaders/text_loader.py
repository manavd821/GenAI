from langchain_community.document_loaders import TextLoader 
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnablePassthrough, RunnableParallel, RunnableBranch, RunnableLambda
load_dotenv()

llm1 = ChatGoogleGenerativeAI(model = 'gemini-2.0-flash').with_fallbacks([ChatGoogleGenerativeAI(model= 'gemma-3-27b-it'),ChatGoogleGenerativeAI(model='learnlm-2.0-flash-experimental') ])
llm2 = ChatGoogleGenerativeAI(model= 'gemma-3-27b-it').with_fallbacks([ChatGoogleGenerativeAI(model='learnlm-2.0-flash-experimental')])
llm3 = ChatGoogleGenerativeAI(model='learnlm-2.0-flash-experimental')


loader = TextLoader(file_path='myfile.txt')
docs = loader.load()
print(docs[0].page_content)
print(docs[0].metadata)

chain = PromptTemplate(
    template='Write a 2 line summary for the following poem - \n{poem}',
    input_variables=['poem']
) | llm2 | StrOutputParser()

print(chain.invoke({'poem' : docs[0].page_content}))
