import os, sys
from dotenv import load_dotenv
from llama_index.core import VectorStoreIndex,SimpleDirectoryReader
import llama_index

load_dotenv()
def main(url : str):
    document = SimpleDirectoryReader(url).load_data()
    index = VectorStoreIndex.from_documents(documents = document)
    query_engin = index.as_query_engine()
    response = query_engin.query('What is directory about?')
    print(response)

if __name__ == '__main__':
    main(url= r'absolute path to any directory')