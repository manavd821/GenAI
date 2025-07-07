from langchain_text_splitters import RecursiveCharacterTextSplitter
from pydantic import BaseModel, Field
from typing import Union
with open('file.txt', 'r') as f:
    text = f.read()


# seps = ['\n\n', '\n', '.',' ']
# def fun(texts : list[str], chunk_size : int = 20, i = 0):
#     if all(len(part) <= chunk_size for part in texts): return texts

#     if i < len(seps):
#         new_texts = []
#         for text in texts:
#             new_texts.extend(text.split(seps[i]))
#         return fun(new_texts, chunk_size, i + 1)

#     # Final fallback: character-level split
#     chunks = []
#     for text in texts:
#         for j in range(0, len(text), chunk_size):
#             chunks.append(text[j : j + chunk_size])
#     return chunks

# print(fun(texts=[text], chunk_size=100))

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 40,
    chunk_overlap = 10
)
result = splitter.split_text(text=text)
print(result)