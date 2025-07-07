from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyMuPDFLoader

with open('file.txt','r+') as f:
    text = f.read()
splitter = CharacterTextSplitter(
    chunk_size = 50,
    chunk_overlap = 10,
    separator=''
)
chunk = splitter.split_text(text=text)
print(chunk)

