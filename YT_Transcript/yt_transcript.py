from youtube_transcript_api import YouTubeTranscriptApi
import streamlit as st, json
from langchain_text_splitters import RecursiveCharacterTextSplitter
# Replace with the actual video ID (not full URL)

# video_id = "2fbrl6WoIyo"
# transcript = YouTubeTranscriptApi.get_transcript(video_id)

# full_text = "\n".join([entry['text'] for entry in transcript])
# splitter = RecursiveCharacterTextSplitter(
#     chunk_size = 100,
#     chunk_overlap = 15
# )
# arr = splitter.split_text(text = full_text)
# with open('file.json','w+') as f:
#     json.dump(arr, f, ensure_ascii=False, indent=4)
#     print('json done')
with open('file.json','r') as f:
    arr_in_string_format = f.read()
    arr = json.loads(s=arr_in_string_format)
    print(type(arr))

st.write(arr)