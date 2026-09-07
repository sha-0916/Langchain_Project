import requests
import streamlit as st

def get_essay_response(input_text):
    response = requests.post(
        "http://localhost:8000/essay",
        json={"topic": input_text}
    )

    return response.json()["answer"]

def get_poem_response(input_text):
    response = requests.post(
        "http://localhost:8000/poem",
        json={"topic": input_text}
    )

    return response.json()["answer"]

st.title("LangChain Demo With Ollama API")

input_text = st.text_input("Write an essay on")
input_text1 = st.text_input("Write a poem on")

if input_text:
    st.write(get_essay_response(input_text))

if input_text1:
    st.write(get_poem_response(input_text1))