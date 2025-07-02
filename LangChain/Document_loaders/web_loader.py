from langchain_community.document_loaders import WebBaseLoader
url = 'https://pypi.org/project/PyPDF2/'
loader = WebBaseLoader(url)
doc = loader.load()
print(len(doc))
print(doc[0].metadata)
page_1 = (doc[0].page_content)
# print(page_1.replace('\n','').replace('\t',''))


from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnablePassthrough, RunnableParallel, RunnableBranch, RunnableLambda
load_dotenv()

llm1 = ChatGoogleGenerativeAI(model = 'gemini-2.0-flash').with_fallbacks([ChatGoogleGenerativeAI(model= 'gemma-3-27b-it'),ChatGoogleGenerativeAI(model='learnlm-2.0-flash-experimental') ])
llm2 = ChatGoogleGenerativeAI(model= 'gemma-3-27b-it').with_fallbacks([ChatGoogleGenerativeAI(model='learnlm-2.0-flash-experimental')])
llm3 = ChatGoogleGenerativeAI(model='learnlm-2.0-flash-experimental')

chain = PromptTemplate(template='{Q}\n{text}',input_variables=['Q','text']) | llm1 | StrOutputParser()
print(chain.invoke({'Q':'What is it about?', 'text' : doc[0].metadata}))
