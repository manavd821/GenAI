from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_experimental.text_splitter import SemanticChunker
from dotenv import load_dotenv
load_dotenv()

model_name = 'text-embedding-004'
embbed_model = GoogleGenerativeAIEmbeddings(model= f'models/{model_name}')
text = """
The Eiffel Tower attracts millions of tourists each year, standing as a symbol of French innovation and design. In contrast, Python’s readability and simplicity make it a favorite among modern developers building AI tools. Meanwhile, the effects of climate change are becoming more visible, with rising sea levels threatening coastal cities. Meditation, when practiced daily, has been shown to reduce stress and improve focus. SpaceX recently tested a new rocket prototype that aims to make interplanetary travel more feasible. On the other hand, proper sleep hygiene, like limiting blue light exposure before bed, can significantly improve overall health.
"""
splitter = SemanticChunker(
    embeddings=embbed_model,
    breakpoint_threshold_type='standard_deviation',
    breakpoint_threshold_amount=0.5
)
result = splitter.create_documents([text])
print(len(result))
print(result)