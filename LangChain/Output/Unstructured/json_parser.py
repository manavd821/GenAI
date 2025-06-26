from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
load_dotenv()
llm = ChatGoogleGenerativeAI(model = 'gemini-2.0-flash')

from langchain_core.output_parsers import JsonOutputParser
parser = JsonOutputParser()


temp1 = PromptTemplate(
    template='Give me name, age and city of a fictional person.\n {format_instruction}',
    input_variables=[],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

# method 1: without chain

# propmt = temp1.format()
# # print(propmt)
# result = llm.invoke(propmt)
# # print(result)
# # print(type(result))
# final_result = parser.parse(result.content)
# print(type(final_result))
# print(final_result)
# print(final_result['name'])

# method 2: with chain
chain = temp1 | llm | parser
result = chain.invoke({})
print(result)

