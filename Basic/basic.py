from google import genai
from dotenv import load_dotenv
import os
import asyncio
load_dotenv()
client = genai.Client(api_key=os.getenv('API_KEY'))

# response = client.models.generate_content(
#     model="gemini-2.0-flash",
#     contents=[
#         {
#             'role' : 'user',
#             'parts' : [{'text' : 'My name is Manav'}]
#         },
#         {
#             'role' : 'model',
#             'parts' : [{'text' : 'Hare Krsna'}]
#         },
#         {
#             'role' : 'user',
#             'parts' : [{'text' : 'What is my name?'}]
#         }
#     ]
# )
# print(response.text)

History = []
async def chatting(userProblem):
    History.append({
        "role" : 'user',
        "parts" : [{"text": userProblem }]
    })
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents = History
        )
        print(response.text)

    except Exception as e:
        print(f"Error in response: {e}")
    
    # print(f"History : {History}\n")

    
async def main():
    userProblem = str(input('Hare Krsna, Ask me anything:'))
    await chatting(userProblem)
    await main()


if __name__ == '__main__':
    asyncio.run(main())  
