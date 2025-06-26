from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

llm1 = ChatGoogleGenerativeAI(model = 'gemini-2.0-flash')
llm2 = ChatGoogleGenerativeAI(model= 'gemma-3-27b-it')
llm3 = ChatGoogleGenerativeAI(model='gemma-3n-e4b-it')

prompt1 = PromptTemplate(
    template='Generate short and simple note from the following text.\n{text}',
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template='Generate 5 short question and answers from the following text.\n{text}',
    input_variables=['text']
)

promp3 = PromptTemplate(
    template='Merge the provided notes and quize into a single document\nnotes -> {notes} and quize -> {quize}',
    input_variables=['notes', 'quize']
)

parser = StrOutputParser()

from langchain.schema.runnable import RunnableParallel

parallel_chain = RunnableParallel({
    'notes' : prompt1 | llm1 | parser,
    'quize' : prompt2 | llm2 | parser
})

merge_chain = promp3 | llm3 | parser

final_chain = parallel_chain | merge_chain
text = """
    Both of these tasks-judging and being judged-are mediated by signals.

A signal, in evolutionary biology, 25 is anything used to communicate or con-vey information. Unblemished skin or fur, for example, is a signal of a healthy organism; compare a prize-winning beagle to a mangy mutt. A growl is a signal of aggression and the growl's depth is a signal of the creature's size.

Signals are said to be honest when they reliably correspond to an underlying trait or fact about the sender. Otherwise they are dishonest or deceptive.

The temptation to deceive is ubiquitous. Deception allows an agent to reap benefits without incurring costs. (See Chapter 5 for more on deception.) That's why the best signals-the most honest ones are expensive. 26 More precisely, they are differentially expensive: costly to produce, but even more costly to fake. 27 A lion's loud, deep growl, for example, is an honest signal of a large body cavity, because it's impossible for a small creature, like a mouse, to make the same sound.

Sometimes it's even necessary to do something risky or wasteful in order to prove that you have a desirable trait. This is known as the handicap principle.28 It explains why species with good defense mechanisms, like skunks and poison dart frogs, evolve high-contrast colors: unless it can defend itself, an animal that stands out quickly becomes another animal's lunch. For a nonbiological example, consider the difference between blue jeans and dress pants. Jeans are durable and don't need to be washed every day, whereas dress pants demand a bit more in terms of upkeep-which is precisely why they're considered more formal attire.

In the human social realm, honest signaling and the handicap principle are best reflected in the dictum, "Actions speak louder than words."22 The problem with words is that they cost almost nothing; talk is usually too cheap. Which is a more honest signal of your value to a company: being told "great job!" or get-

ting a raise?

We rely heavily on honest signals in the competitive arenas we've been discussing-that is, whenever we try to evaluate others as potential mates, friends, and allies. Loyal friends can distinguish themselves from fair-weather friends by visiting you in the hospital, for example. Healthy mates can distin-guish themselves from unhealthy ones by going to the gym or running a mara-thon. Initiates who get gang tattoos thereby commit themselves to the gang in a way that no verbal pledge could hope to accomplish. Of course, we also use these honest signals whenever we wish to advertise our own value as a friend, mate, or teammate.

Note that we don't always need to be conscious of the signals we're sending and receiving. We may have evolved an instinct to make art, for example, as a means of advertising our artistic skills and free time (survival surplus)-but that's not necessarily what we're thinking about as we whittle a sculpture from a piece of driftwood. We may simply be thinking about the beauty of the sculp-ture (for more on art, see Chapter 11). Nevertheless, the deeper logic of many of our strangest and most unique behaviors may lie in their value as signals.
"""
result = final_chain.invoke({'text': text})
# print(result)

final_chain.get_graph().print_ascii()
