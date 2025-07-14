from langchain_google_genai import GoogleGenerativeAIEmbeddings
from youtube_transcript_api import YouTubeTranscriptApi
from langchain_text_splitters import RecursiveCharacterTextSplitter
import json
# Replace with the actual video ID (not full URL)

video_id = "2fbrl6WoIyo"
# transcript = YouTubeTranscriptApi.get_transcript(video_id)

# with open('text.json', 'w') as f:
#     json.dump(transcript, f , indent=4)
#     print('json ingest successful')

cricketers = [
    "Virat Kohli - Indian batting maestro known for his aggression and consistency across formats.",
    "MS Dhoni - Legendary Indian captain and finisher, known for calmness and helicopter shots.",
    "Sachin Tendulkar – The 'God of Cricket' with 100 international centuries to his name.",
    "Rohit Sharma – Indian opener famous for effortless timing and multiple double centuries in ODIs.",
    "Ben Stokes – England's fiery all-rounder known for heroic performances in high-pressure games.",
    "Kane Williamson – New Zealand’s calm and technically sound captain and top-order batsman.",
    "Steve Smith – Australia’s unconventional genius with incredible Test match consistency.",
    "AB de Villiers – South African ‘Mr. 360°’ known for explosive and innovative stroke play.",
    "Jasprit Bumrah – Indian pacer with deadly yorkers and unmatched death-over skills.",
    "Rashid Khan – Afghan leg-spinner who dominates T20 leagues worldwide with tight control.",
    "Joe Root – England’s classy right-hander and dependable backbone of the Test team.",
    "Babar Azam – Pakistan’s elegant and consistent top-order batsman across all formats.",
    "Hardik Pandya – Indian all-rounder known for explosive hitting and handy seam bowling.",
    "Pat Cummins - Australian pace spearhead and captain with a deadly mix of speed and control.",
    "Shubman Gill - Young Indian prodigy admired for stylish stroke play and solid temperament."
]

model_name = 'text-embedding-004'
# model = GoogleGenerativeAIEmbeddings(model= f'models/{model_name}')
# emb = model.embed_documents(cricketers)
# print(len(emb[0]))
# with open('embd.json','w') as f:
#     json.dump(emb, f, indent=4)

with open('embd.json','r') as f:
    emb_vector = json.load(f)
print(len(emb_vector[0]))

# qdrant start
from qdrant_client import QdrantClient
client = QdrantClient(host='localhost', port=6333)
# check if collection exists
print(client.collection_exists(collection_name='cricketer_db'))
# client.recreate_collection(
#     collection_name="cricketer_db",
#     vectors_config={
#         'size' : len(emb_vector[0]),
#         'distance' : 'Cosine'
#     }
# )
# collection = client.get_collection()
