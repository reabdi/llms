import os
from langchain_community.llms import OpenAI
import streamlit as st
# Loading environment variables
from dotenv import (
    load_dotenv,
)  # Dotenv for loading environment variables from a .env file

load_dotenv()  # Load environment variables from .env file

# streamlit framework
st.title("Langchain Demo with OpenAI API")
input_text = st.text_input("Search the topic you want...")

# OpenAI LLM Implementation
llm = OpenAI(temperature=0.7)

if input_text:
    st.write(llm(input_text))