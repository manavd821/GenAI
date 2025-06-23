from dotenv import load_dotenv
import streamlit as st, asyncio
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate, load_prompt
load_dotenv()

model_name = 'gemini-2.0-flash'
llm = ChatGoogleGenerativeAI(model=model_name)

st.header('Research Tool:')

# user_input = st.text_input(placeholder='Enter Your Query', label='Enter Your prompt:')
paper_input = st.selectbox(label='Select research paper name:',options=[
    "Attention Is All You Need",
    "Language Models are Few-Shot Learners",
    "AutoGPT: The Role of LLMs as Autonomous Agents",
    "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks",
    "Scaling Laws for Neural Language Models"
    ])
input_style = st.selectbox('Select explanation style',options=[
    "Beginner Friendly",
    "Code Oriented",
    "Mathematical Perspective",
    "Real-world Use Cases",
    "Step-by-step Breakdown",
    "Analogy Based",
    "Visual Explanation",
    "Implementation Guide",
    "Theoretical Deep Dive",
    "Research-to-Production Transition"
])
input_length = st.selectbox('Select explanation length:', options=[
    "Very Short (1-2 lines)",
    "Short Summary",
    "Medium (Detailed Overview)",
    "Long (In-depth Explanation)",
    "Full Paper Walkthrough"
])
# Method 1

template = load_prompt('LangChain\Prompt\\template.json')
# fill the placeholder
prompt = template.invoke({
    'paper_input': paper_input,
    'input_style': input_style,
    'input_length' : input_length
})


# Method 2
# prompt = PromptTemplate.from_template("""
# You are an expert in Generative AI and NLP research papers.

# # Your task is to explain the paper titled "{paper_input}".

# The explanation should be:
# - Styled as "{input_style}"
# - With a length of "{input_length}"

# Be clear, accurate, and focused on delivering value to the reader.

# Use real examples, analogies, equations, or code where needed depending on the style.

# Avoid unnecessary jargon unless it fits the selected style.

# Start the explanation now.
# """)
# formatted_prompt = prompt.format(paper_input = paper_input, input_style = input_style, input_length = input_length)

# method 2 from json file
# prompt = load_prompt('LangChain\Prompt\\template.json')
# formatted_prompt = prompt.format(paper_input = paper_input, input_style = input_style, input_length = input_length)

if st.button(label='summerize'):
    chain = template | llm
    result =chain.invoke({
    'paper_input': paper_input,
    'input_style': input_style,
    'input_length' : input_length
})
    # result = llm.invoke(prompt)
    # result = llm.invoke(formatted_prompt)
    st.write(result.content)