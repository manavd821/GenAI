from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel
load_dotenv()

llm1 = ChatGoogleGenerativeAI(model = 'gemini-2.0-flash')
llm2 = ChatGoogleGenerativeAI(model= 'gemma-3-27b-it')
# prompt1 = PromptTemplate(
#     template='Generate a short tweet about {topic}',
#     input_variables=['topic']
# )
# prompt2 = PromptTemplate(
#     template='Generate a short LinkedIn about {topic}',
#     input_variables=['topic']
# )
# parser = StrOutputParser()

# parallel_chain = RunnableParallel({
#     'tweet' : RunnableSequence(prompt1, llm2, parser),
#     'LinkedIn' : RunnableSequence(prompt2, llm2, parser)
# })

# result = parallel_chain.invoke({'topic' : 'AI'})
# print(result['tweet'], end='\n\n')
# print(result['LinkedIn'])

# Another example
feedback_generation = PromptTemplate(
    template='Write a negative feedback about {product} in few lines',
    input_variables=['product']
)
feedback_generation_chain = feedback_generation | llm1 | StrOutputParser()
rate_feedback_prompt = PromptTemplate(
    template="Rate the following feedback out of 10 based on its quality. Only rate, don't give any explaination\n{feedback}",
    input_variables=['feedback']
)
response_feedback_prompt = PromptTemplate(
    template='Respond to the below feedback of customer appropriately in few lines.\n{feedback}',
    input_variables=['feedback']
)
# method-1
# analyze_feedback_final_chain = feedback_generation_chain | RunnableParallel({
#     'rate': rate_feedback_prompt | llm1 | StrOutputParser(),
#     'response' : response_feedback_prompt | llm2 | StrOutputParser()
# })
# analyze_feedback = analyze_feedback_final_chain.invoke({'product' : 'Headphone'})

# method-2
# analyze_feedback_final_chain = feedback_generation_chain | {
#     'rate': rate_feedback_prompt | llm1 | StrOutputParser(),
#     'response' : response_feedback_prompt | llm2 | StrOutputParser()
# }
# analyze_feedback = analyze_feedback_final_chain.invoke({'product' : 'Headphone'})


# method-3
# analyze_feedback_final_chain = feedback_generation_chain | RunnableParallel(
#     rate = rate_feedback_prompt | llm1 | StrOutputParser(),
#     response = response_feedback_prompt | llm2 | StrOutputParser()
# )
# analyze_feedback = analyze_feedback_final_chain.invoke({'product' : 'Headphone'})

# print('rating: ', analyze_feedback['rate'])
# print('response: ', analyze_feedback['response'])