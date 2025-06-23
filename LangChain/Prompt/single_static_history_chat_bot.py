from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import asyncio
load_dotenv()
llm = ChatGoogleGenerativeAI(model = 'gemini-2.0-flash')
history = []
while True:
    user_input = str(input('Enter your query: '))
    if user_input == 'exit':
        print(history)
        break
    history.append({
        'model' : 'How can I assist you?',
        'user' : user_input
    })
    result = (llm.invoke(history))
    history.append(result.content)
    print('AI: ', result.content)