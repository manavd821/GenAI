from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()

llm = HuggingFaceEndpoint(  
    repo_id="microsoft/Phi-3-mini-4k-instruct",  
    task="text-generation",  
    max_new_tokens=10,  
    do_sample=False,  
    repetition_penalty=1.03,  
) 
model = ChatHuggingFace(llm=llm, verbose=True)

result = model.invoke('What is capital of India?')
print(result)