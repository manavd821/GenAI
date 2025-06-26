from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

load_dotenv()
llm = ChatGoogleGenerativeAI(model = 'gemini-2.0-flash')

# method 1 : manual method
# temp1 = PromptTemplate(
#     template='Write detail report on {topic}',
#     input_variables=['topic'],
#     validate_template=True
# )
# temp2 = PromptTemplate(
#     template='Write 5 line summary on following text.\n {text}',
#     input_variables=['text'],
#     validate_template=True
# )
# prompt1 = temp1.invoke({'topic' : 'black hole'})
# result1 = llm.invoke(prompt1)
# print('result 1:\n', result1)

# prompt2 = temp2.invoke({'text' : result1.content})
# result2 = llm.invoke(prompt2)
# print('\n\n\n',result2.content)

# method 2: Inbuilt method

from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()
temp1 = PromptTemplate(
    template='Write detail report on {topic}',
    input_variables=['topic'],
    validate_template=True
)
temp2 = PromptTemplate(
    template='Write 5 line summary on following text.\n {text}',
    input_variables=['text'],
    validate_template=True
)
chain = temp1 | llm | parser | temp2 | llm | parser
result = chain.invoke({'topic' : 'black hole'})
print(result)