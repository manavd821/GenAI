from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
load_dotenv()
llm = ChatGoogleGenerativeAI(model = 'gemini-2.0-flash')

prompt1 = PromptTemplate(
    template='Generate a detail report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a 5 pointer summary from the following text.\n {text}',
    input_variables=['text']
)
from langchain_core.output_parsers import StrOutputParser
parser = StrOutputParser()

chain = prompt1 | llm | parser | prompt2 | llm | parser

result = chain.invoke({'topic' : 'Attension all you need'})
# print(result)

chain.get_graph().print_ascii()