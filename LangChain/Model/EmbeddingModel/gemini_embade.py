from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
load_dotenv()

model_name = 'text-embedding-004'
embbed_model = GoogleGenerativeAIEmbeddings(model= f'models/{model_name}')

query = 'Tell me about Dhoni'
document = [
    "Sachin Tendulkar is regarded as one of the greatest batsmen in history.",
    "Virat Kohli is renowned for his modern-day run-scoring consistency and aggressive captaincy.",
    "MS Dhoni is celebrated for his calm demeanor and exceptional finishing skills as a wicketkeeper-batsman.",
    "Shane Warne was an Australian leg-spinner who mesmerized the world with his mastery of spin bowling.", 
    "Sir Donald Bradman holds an unparalleled Test batting average of 99.94."
]

queary_vector = embbed_model.embed_query(query)
docs_vector = embbed_model.embed_documents(document)
# print(queary_vector)
# print(len(docs_vector))
# for doc in docs_vector:
#     vector = doc
#     print(f'vector dimension: {len(vector)}')
#     print(vector, end = '\n\n')
similarity = cosine_similarity([queary_vector], docs_vector)
similarity_list = list(enumerate(similarity[0]))
sorted_vector = sorted(similarity_list, key=lambda x: x[-1], reverse=True)
# print(sorted_vector)
index = sorted_vector[0][0]
score = sorted_vector[0][1]
print(query)
print(document[index])
print(f'similarity score: {score}')