from langchain_google_genai import ChatGoogleGenerativeAI
from typing import TypedDict, Annotated, List, Optional, Literal
from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv()

llm = ChatGoogleGenerativeAI(model = 'gemini-2.0-flash')
# json schema
json_schema = {
  "title": "Review",
  "type": "object",
  "properties": {
    "key_themes": {
      "type": "array",
      "items": { "type": "string" },
      "description": "Write down atleast 5 key themes discussed in the review in a list"
    },
    "summary": {
      "type": "string",
      "description": "A brief summary of the review"
    },
    "sentiment": {
      "type": "string",
      "enum": ["positive", "negative"],
      "description": "Return sentiment of review either positive, negative or neutral"
    },
    "pros": {
      "type": "array",
      "items": { "type": "string" },
      "description": "Write down all the pros inside a list"
    },
    "cons": {
      "type": "array",
      "items": { "type": "string" },
      "description": "Write down all the cons inside a list"
    },
    "name": {
      "type": "string",
      "description": "Write name of reviewer"
    }
  },
  "required": ["key_themes", "summary", "sentiment"]
}



structured_model = llm.with_structured_output(json_schema)

result = structured_model.invoke('''
Artificial Intelligence (AI) has transformed how we interact with technology, offering solutions that were once considered science fiction. It powers everything from virtual assistants and personalized recommendations to advanced tools in healthcare, finance, and education. AI systems can process massive amounts of data quickly, identify patterns, and make decisions faster and more accurately than humans in many scenarios. This has led to increased efficiency, automation of repetitive tasks, and innovation across nearly every industry. For example, AI-driven diagnostics in medicine have helped detect diseases earlier, while predictive maintenance in manufacturing has reduced downtime and costs.

However, the rapid expansion of AI comes with serious downsides. One major concern is the displacement of human jobs, especially in industries dependent on routine labor. As companies adopt AI to cut costs, many workers face unemployment or the need for re-skilling. Furthermore, AI can inherit biases from the data it is trained on, leading to unfair outcomes in sensitive areas like hiring, policing, or lending. Privacy is another significant issue—AI technologies used in surveillance, facial recognition, or data tracking can be misused to violate individual freedoms. The lack of transparency in how some AI models make decisions also makes it difficult to hold anyone accountable when things go wrong.

✅ Pros of AI:
Boosts efficiency and productivity

Automates repetitive and dangerous tasks

Improves decision-making through data analysis

Enhances healthcare, finance, education, etc.

Enables innovation in areas like robotics and self-driving cars

❌ Cons of AI:
Job loss and economic disruption

Algorithmic bias and discrimination

Threats to privacy and personal data

Lack of transparency and accountability

Potential misuse in surveillance and warfare

Reviewed by Manav Desai
''')
print(len(result))
answer = result[0]['args']
print(type(result))
print(answer['summary'])