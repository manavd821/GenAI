import os
from dotenv import load_dotenv

from llama_index.readers.web import SimpleWebPageReader
from llama_index.core import VectorStoreIndex
import llama_index

load_dotenv()
def main(url : str):
    document = SimpleWebPageReader(html_to_text = True).load_data(urls = [url])
    index = VectorStoreIndex.from_documents(documents = document)
    query_engin = index.as_query_engine()
    response = query_engin.query('How Traditional Machine Learning Works?')
    print(response)

if __name__ == '__main__':
    main(url= 'https://medium.com/@prajwalkankate/what-is-genai-7e10f008e749')