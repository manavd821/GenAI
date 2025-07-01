from dotenv import load_dotenv
import streamlit as st, asyncio
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate, load_prompt, ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from pydantic import BaseModel, Field
from typing import List, Annotated, Optional
from langchain.schema.runnable import RunnableParallel, RunnablePassthrough, RunnableLambda
load_dotenv()

def all_fallback():
    return ("There is some error in model." "Please try again later")

model_name = 'gemini-2.0-flash'
llm = ChatGoogleGenerativeAI(model=model_name).with_fallbacks([ChatGoogleGenerativeAI(model='gemma-3-27b-it'),ChatGoogleGenerativeAI(model='learnlm-2.0-flash-experimental'), RunnableLambda(all_fallback)])

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
text = """
# You are an expert in Generative AI and NLP research papers.

# # Your task is to explain the paper titled "{paper_input}".

# The explanation should be:
# - Styled as "{input_style}"
# - With a length of "{input_length}"

# Be clear, accurate, and focused on delivering value to the reader.

# Use real examples, analogies, equations, or code where needed depending on the style.

# Avoid unnecessary jargon unless it fits the selected style.

# Start the explanation now.
# """
template = PromptTemplate(
    template=text,
    input_variables=['paper_input', 'input_style', 'input_length']
)

class Review(BaseModel):
    key_aspects : list[str] = Field(description='Write key aspects discussed in the summary',examples=["Data Collection","Data Preprocessing","Model Training","Model Evaluation","Deployment","Monitoring & Maintenance"])
    pros : Annotated[Optional[list[str]], "Write down all the pros inside a list"]
    cons : Annotated[Optional[list[str]], "Write down all the cons inside a list"]

parser = PydanticOutputParser(pydantic_object=Review)

review_prompt = PromptTemplate(
    template='Write review on following summary in given formate.\nfeedback:\n {feedback}\nformate:\n{format}',
    input_variables=['feedback'],
    partial_variables={'format' : parser.get_format_instructions()}
) 

if st.button(label='summerize'):
    summary_chain = template | llm | StrOutputParser()
    final_chain = RunnableParallel({
        'summary' : summary_chain,
        'review' : summary_chain | review_prompt | llm | parser
    })
    result =final_chain.invoke({
    'paper_input': paper_input,
    'input_style': input_style,
    'input_length' : input_length
})

    review = result['review']
    summary = result['summary']
    st.write(summary)
    key_aspects = ", ".join(str(aspect) for aspect in review.key_aspects)
    pros = ", ".join(str(pro) for pro in review.pros)
    cons = " ".join(str(con) for con in review.cons)
    st.write(f'key aspects: {key_aspects}')
    st.write(f'pros: {pros}')
    st.write(f'cons: {cons}')
