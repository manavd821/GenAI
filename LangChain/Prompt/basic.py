from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain.memory import ConversationBufferMemory
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash')
# tricks:1) .formate : direct str ave
#         .invoke({}) : text = ...(In PromptTemplate) or messages = ...(In CharPromptTemplate)

# 2). PromptTemplate ->single msg
#     ChatPromptTemplates ->multiple msg(e.g. you provide examples to llm)   


# Single static messges
# temp1 = PromptTemplate.from_template(template='Explain {var1} and {var2} in few words.').format(var1 = 'val1', var2 = 'val2')
# print(temp1)

# temp2 = PromptTemplate.from_template(template='Explain {var1} and {var2} in few words.').invoke({'var1' : 'val1', 'var2' : 'val2'})
# print(temp2)

# temp3 = PromptTemplate(template='Explain about {var3} and {var4} in few words', input_variables=['var3','var4'], validate_template=True).format(var3='val3', var4 = 'val4')
# print(temp3)

# temp4 = PromptTemplate(template='Explain about {var3} and {var4} in few words', input_variables=['var3','var4'], validate_template=True).invoke({'var3':'val3', 'var4' : 'val4'})
# print(temp4)

# # multi static messages history
# # re = llm.invoke(input=[SystemMessage(content='You are a proffesional doctor'), HumanMessage(content='My leg is paining, help me in few words.')])
# # print(re.content)
# # AIMessage(content=re.content)


# # Single Dynamic messages
# examples = [
#     {"question": "What is AI?", "answer": "AI is a branch of CS that simulates intelligence."},
#     {"question": "What is ML?", "answer": "ML is a subset of AI focused on learning from data."}
# ]
# example_prompt_from_PromptTemplates = PromptTemplate(input_variables=['question','answer'], template='Q: {question}\nA: {answer}', validate_template=True)
# final_prompt = FewShotPromptTemplate(
#     prefix = 'You are helpful assistant.',
#     examples = examples,
#     example_prompt = example_prompt_from_PromptTemplates,
#     example_separator = '\n',
#     suffix="Q: {user_question}\nA:",
#     input_variables = ['user question']
# ).format(user_question = 'What is Deep learning?')
# print('\n',final_prompt)

# multi - messages history
# chTemp1 = ChatPromptTemplate([
#     ('system','you are a helpful assisntant. Your name is {name}'),
#     ("human", "Hello, how are you doing?"),
#     ("ai", "I'm doing well, thanks!"),
#     ("human", "{user_input}"),
# ]).invoke({'name': 'Manav', 'user_input' : 'What is your name?'})
# print(chTemp1)

# chTemp2 = ChatPromptTemplate([
#     ('system','you are a helpful assisntant. Your name is {name}'),
#     ("human", "Hello, how are you doing?"),
#     ("ai", "I'm doing well, thanks!"),
#     ("human", "{user_input}"),
# ]).format(name='Manav', user_input = 'What is your name?')
# print(chTemp2)

# chTemp3 = ChatPromptTemplate([
#     ("system", "You are a helpful AI bot."),
#     ('placeholder', '{conversation}')
# ]).invoke({'conversation' : [
#                         ("human", "Hi!"),
#                         ("ai", "How can I assist you today?"),
#                         ("human", "Can you make me an ice cream sundae?"),
#                         ("ai", "No.")
#                     ]}) # you can use .formate here
# print(chTemp3)

# chTemp4 = ChatPromptTemplate.from_messages([
#     ("system", "You are a helpful assistant."),
#     ("human", "Explain {concept} in simple terms in {way}")
# ]).format_messages(concept="transformers", way='few words.')
# print(chTemp4)

# MessagePlaceholder
# msgTemp1 = MessagesPlaceholder(variable_name='history').format_messages() => raise KeyError
# msgTemp1 = MessagesPlaceholder(variable_name='history', optional=True).format_messages()  # Returns empty list
# print(msgTemp1)

# msgTemp2 = MessagesPlaceholder(variable_name='history').format_messages(history=[
#                     ("system", "You are an AI assistant."),
#                     ("human", "Hello!"),
#                 ])
# print(msgTemp2)


# msgTemp2 = ChatPromptTemplate([
#     ("system", "You are a mathematics teacher."),
#     MessagesPlaceholder(variable_name='chat_history'),
#     ("human", "{queary}")
# ]).invoke({
#     'chat_history': [
#         ("human", "what's 5 + 2"),
#         ("ai", "5 + 2 is 7")
#     ],
#     'queary' :  'Now, multiply that by 4'
# })
# print(msgTemp2)

# fetch chat history from another file(used in DB interactions) => Alternative of msgTemp2
chat_template = ChatPromptTemplate([
    ("system", "You are a mathematics teacher."),
    MessagesPlaceholder(variable_name='chat_history_in_file'),
    ("human", "{query}")
])
chat_history_in_file = []
# load chat history from file
with open('chat_history.txt') as f:
    chat_history_in_file.extend(f.readlines())
# print('chat_history_in_file: ',chat_history_in_file)

msgTemp3 = chat_template.invoke({
    'chat_history_in_file' : chat_history_in_file,
    'query' : 'Now, multiply that by 4'
})
print(msgTemp3)
