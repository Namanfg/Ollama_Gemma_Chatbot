from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser

import streamlit as st 
import os
from dotenv import load_dotenv

load_dotenv()

# os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
#langsmith 
os.environ["LANGCHAIN_TRACING_V2"]="true"


## Prompt Template

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please respond to the user queries"),
        ("user","Question:{question}")
    ]
)

st.title("Langchain Demo using Ollama")
input_text=st.text_input("Search the topic you want")


# llm
llm = Ollama(model="gemma")
output_parser = StrOutputParser()
chain=prompt|llm|output_parser
if input_text:
    st.write(chain.invoke({'question':input_text}))