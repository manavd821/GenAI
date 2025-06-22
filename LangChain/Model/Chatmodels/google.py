from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(model='gemma-3n-e4b-it', temperature=0)
result = model.invoke('Write five line poem on cricket.')
print(result.content)