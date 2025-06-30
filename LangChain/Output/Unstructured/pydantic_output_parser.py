from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
load_dotenv()
llm = ChatGoogleGenerativeAI(model = 'gemini-2.0-flash')


from langchain_core.output_parsers import PydanticOutputParser, StrOutputParser
from pydantic import BaseModel, Field

class Person(BaseModel):
    name : str = Field(description='Name of the person')
    age : int = Field(gt = 18, description='Age of the person')
    city: str = Field(description='Name of the city the person belong to')

parser = PydanticOutputParser(pydantic_object=Person)
# print(parser.get_format_instructions())

template = PromptTemplate(
    template='Generate the name, age and city of a fictional {place} person.\n{format_instruction}',
    input_variables=['place'],
    partial_variables={'format_instruction' : parser.get_format_instructions()}
)

# final short-answer => This runnable converts everything to what you want
# chain = template | llm | parser
# result = chain.invoke({'place' : 'India'})
# # print(type(result))
# print(result.content)

chain2 = template | llm | StrOutputParser()
result2 = chain2.invoke({'place': 'India'})
print('original response from llm(in json but not clean): ', type(result2))
print('llm response in Json Formate:\n',result2)

# parses json to pydantic object
pyresult2 = parser.parse(result2) 
print('pydantic object: ',type(pyresult2))
print('Pydantic Formate:\n',pyresult2)

# Cleaning llm response
clean_json = result2.replace('json','').replace('`','').replace('\n','')
print('After cleaning to clear json: ',type(clean_json))
print(clean_json)

# parses json to python dictionary 
import json
pyresult2 = json.loads(clean_json)
print('python dict: ',type(pyresult2))
print(pyresult2)


