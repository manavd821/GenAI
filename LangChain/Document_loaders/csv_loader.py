from langchain_community.document_loaders import CSVLoader

loader = CSVLoader('profile.csv')
docs = loader.load()
print(len(docs))
# print(docs[-1].page_content)
for doc in docs:
    print(doc.page_content.replace('\n',''))