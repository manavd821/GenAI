from langchain_core.prompts import PromptTemplate


template = PromptTemplate(template="""
You are an expert in Generative AI and NLP research papers.

Your task is to explain the paper titled "{paper_input}".

The explanation should be:
- Styled as "{input_style}"
- With a length of "{input_length}"

Be clear, accurate, and focused on delivering value to the reader.

Use real examples, analogies, equations, or code where needed depending on the style.

Avoid unnecessary jargon unless it fits the selected style.

Start the explanation now.
""",
input_variables=['paper_input', 'input_style', 'input_length'],
validate_template=True
)

template.save('template.json')