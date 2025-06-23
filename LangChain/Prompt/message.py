from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()
llm = ChatGoogleGenerativeAI(model = 'gemini-2.0-flash')

chat_history = [
    SystemMessage(content='You are a helpful assitant')
]
while True:
    user_input = str(input('Ask anything:'))
    if user_input == 'exit':
        break
    chat_history.append(HumanMessage(content=user_input))
    result = llm.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print('AI: ', result.content)

print(chat_history)