from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(model='gemma-3n-e4b-it')
result = model.invoke('What is capital of India?')
print(result)