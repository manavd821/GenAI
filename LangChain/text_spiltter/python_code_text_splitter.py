from langchain_text_splitters import RecursiveCharacterTextSplitter, Language
# with open('length_based.py','r') as f:
#     code = f.read()

code = """
def recursive_split(text, chunk_size=100, chunk_overlap=20, separators=None):
    if separators is None:
        separators = ['\n\n', '\n', '.', ' ', '']  # fallback to character-level

    def split_with_separator(txt, sep):
        return txt.split(sep) if sep else list(txt)

    def merge_chunks(chunks):
        final = []
        current = ''
        for chunk in chunks:
            if len(current) + len(chunk) <= chunk_size:
                current += chunk + separator  # add back the separator
            else:
                if current:
                    final.append(current.strip())
                current = chunk + separator
        if current:
            final.append(current.strip())
        return final

    # Try each separator in order
    for separator in separators:
        parts = split_with_separator(text, separator)
        if all(len(p) <= chunk_size for p in parts):
            return merge_chunks(parts)

    # Final fallback: hard cut (no good separator found)
    chunks = []
    for i in range(0, len(text), chunk_size - chunk_overlap):
        chunks.append(text[i:i + chunk_size])
    return chunks
"""
splitter = RecursiveCharacterTextSplitter.from_language(
    language = Language.PYTHON,
    chunk_size = 170,
    chunk_overlap = 0 
)
result = splitter.split_text(code)
print(result)