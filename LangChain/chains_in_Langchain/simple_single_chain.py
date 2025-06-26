from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
load_dotenv()
llm = ChatGoogleGenerativeAI(model = 'gemini-2.0-flash')

prompt = PromptTemplate(
    template='Generate 5 interesting facts about {topic}',
    input_variables=['topic']
)
from langchain_core.output_parsers import StrOutputParser
parser = StrOutputParser()

chain = prompt | llm | parser

result = chain.invoke({'topic' : 'cricket'})
print(result)

# print chain steps: install pip install grandalf
chain.get_graph().print_ascii()