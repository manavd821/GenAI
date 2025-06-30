from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import (RunnableSequence, RunnablePassthrough, RunnableParallel, RunnableLambda, RunnableWithFallbacks)
load_dotenv()

llm1 = ChatGoogleGenerativeAI(model = 'gemini-2.0-flash')
llm2 = ChatGoogleGenerativeAI(model= 'gemma-3-27b-it')
llm3 = ChatGoogleGenerativeAI(model='learnlm-2.0-flash-experimental')

def when_all_is_failed(inputs):
    return ("Looks like our LLM providers are down. "
                        "There may be any problem"
                        "Please try again later.")
# method 1 -> with_fallback
llm4 = ChatAnthropic(model='claude-3.5-sonnet-20241022').with_fallbacks([ChatGoogleGenerativeAI(model = 'gemini-2.0-flash'), ChatGoogleGenerativeAI(model='gemma-3-27b-it'), RunnableLambda(when_all_is_failed)])

chain_with_fallback1 = (PromptTemplate(template='Tell me joke about {topic}') | llm4 | StrOutputParser()).with_fallbacks([RunnableLambda(when_all_is_failed)])
print(chain_with_fallback1.invoke({}))

# method 2 -> RunnableWithFallbacks
chain_with_fallback2 = RunnableWithFallbacks(runnable= (PromptTemplate(template='Tell me joke about {topic}') | llm4 | StrOutputParser()), fallbacks=[RunnableLambda(when_all_is_failed)])
print(chain_with_fallback2.invoke({}))
