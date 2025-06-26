from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
load_dotenv()
llm = ChatGoogleGenerativeAI(model = 'gemini-2.0-flash')


from langchain.output_parsers import StructuredOutputParser, ResponseSchema
schema = [
    ResponseSchema(name='fact_1', description='Fact 1 about the topic'),
    ResponseSchema(name='fact_2', description='Fact 2 about the topic'),
    ResponseSchema(name='fact_3', description='Fact 3 about the topic')
]

parser = StructuredOutputParser.from_response_schemas(response_schemas=schema)

prompt = PromptTemplate(
    template='Give 3 fact about {topic}.\n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction' : parser.get_format_instructions()},
    validate_template=True
).invoke({'topic' : 'black hole'})

result = llm.invoke(prompt)
print('result:\n',result)
final_result = parser.parse(result.content)
print('final_result:\n',final_result)