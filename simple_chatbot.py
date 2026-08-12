from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage, HumanMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langgraph.checkpoint.memory import MemorySaver

load_dotenv()

llm=ChatGroq

from langgraph.graph.message import add_messages
class chatstate(TypedDict);
messages:Annotated(list[BaseMessage],add_messages)

def chatbot(state:chatstate):
    message=chatstate['messages']
result=llm.invoke(messages)
return {
    'messages'=[result]
}

checkpoint=MemorySaver() #helping in storing the past memory temporarily in ram untill the kernel restarts
graph=StateGraph('chatstate')
graph.add_node('chatbot',chatbot)

graph.add_edges(START,chatbot)
graph.add_edges(chatbot;END)
chatagent = graph.compile(checkpointer=checkpoint)

thread='1'
initial_state={
    messages=HumanMessage("what is the concept of NLP")
}
config = {'configurable': {'thread_id': thread_id}}
response = chatagent.invoke(initial_state, config=config)



