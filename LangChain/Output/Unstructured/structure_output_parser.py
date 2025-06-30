from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
load_dotenv()
llm = ChatGoogleGenerativeAI(model = 'gemini-2.0-flash')


from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain_core.output_parsers import StrOutputParser
schema = [
    ResponseSchema(name='fact_1', description='Fact 1 about the topic'),
    ResponseSchema(name='fact_2', description='Fact 2 about the topic'),
    ResponseSchema(name='fact_3', description='Fact 3 about the topic')
]

parser = StructuredOutputParser.from_response_schemas(response_schemas=schema)

template = PromptTemplate(
    template='Give 3 fact about {topic} in one line.\n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction' : parser.get_format_instructions()},
    validate_template=True
)
# prompt = template..invoke({'topic' : 'black hole'})

# result = llm.invoke(prompt)
# print('result:\n',result)
# print('original llm response type:',type(result))
# final_result = parser.parse(result.content) # converts unclean json to python dict
# print('final_result:\n',final_result)
# print('final_result type:',type(final_result))

# chain = template | llm | StrOutputParser()
# result = chain.invoke({'topic': 'black hole'})
# print('unclean json:\n',result)
# final_result = parser.parse(result) # converts unclean json to python dict
# print('python dict: ',type(final_result))
# print('python dict: ',(final_result))

# final short-answer => This runnable converts everything to what you want
chain = template | llm | parser
print(chain.invoke({'topic' : 'Black hole'}))