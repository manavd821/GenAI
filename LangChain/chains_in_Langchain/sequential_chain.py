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

# result = chain.invoke({'topic' : 'Attension all you need'})
# print(result)

chain.get_graph().print_ascii()

# print('get_config_jsonschema: ',chain.get_config_jsonschema(), end='\n\n')
# print('config_schema: ',chain.config_schema(), end='\n\n')
# print('get_output_jsonschema: ', chain.get_output_jsonschema(), end='\n\n')
# print('get_input_jsonschema: ', chain.get_input_jsonschema(), end='\n\n')
# print('get_input_schema: ', chain.get_input_schema(), end='\n\n')
# print('input_schema: ', chain.input_schema, end='\n\n')
