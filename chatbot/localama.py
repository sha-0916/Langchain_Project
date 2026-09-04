from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

#Prompt Template
prompt=ChatPromptTemplate.from_messages(
    [   
        ("system","You are a helpful assistant. Please response to the user queries"),
        ("user","Question:{question}")
    ]   
)

#streamlit framework
st.title('Langchain Demo With Ollama API')
input_text=st.text_input("Search the topic u want")

#ollama LLm
llm=ChatOllama(model="llama3.2")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))


