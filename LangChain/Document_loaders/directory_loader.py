from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='books',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)
docs = loader.lazy_load()
# print(len(doc))
# print(doc[6].page_content)
# print(doc[6].metadata)
for doc in docs:
    print(doc.metadata)