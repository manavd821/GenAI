from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import os

os.environ['HF_HOME'] = 'D:/huggingface_cache'
llm = HuggingFacePipeline.from_model_id(
    model_id = 'TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    task = 'text-generation',
    # model_kwargs={"device": 0}, 
    pipeline_kwargs = dict(
        max_new_tokens = 20
    )
)
model = ChatHuggingFace(llm=llm)

result = model.invoke('What is capital of India?')
print(result)
