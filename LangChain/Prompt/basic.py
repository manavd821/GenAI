from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()


temp1 = PromptTemplate.from_template(template='Explain {var1} and {var2} in few words.').format(var1 = 'val1', var2 = 'val2')
print(temp1)
temp2 = PromptTemplate.from_template(template='Explain {var1} and {var2} in few words.').invoke({'var1' : 'val1', 'var2' : 'val2'})
print(temp2)

temp3 = PromptTemplate(template='Explain about {var3} and {var4} in few words', input_variables=['var3','var4'], validate_template=True).invoke({'var3':'val3', 'var4' : 'val4'})
print(temp3)