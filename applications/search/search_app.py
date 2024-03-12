import os
from langchain_community.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain, SequentialChain
from langchain.memory import ConversationBufferMemory

import streamlit as st
# Loading environment variables
from dotenv import (
    load_dotenv,
)  # Dotenv for loading environment variables from a .env file

load_dotenv()  # Load environment variables from .env file

# streamlit framework
st.title("Celibrity Seach")
input_text = st.text_input("Search the topic you want...")

# OpenAI LLM Implementation
llm = OpenAI(temperature=0.7)

# PromptTemplate
first_input = PromptTemplate(
    input_variables = ['name'],
    template = """
    You are a useful assistant. Tell me about celebtity {name}
    """
)

# Memory
person_memory = ConversationBufferMemory(input_key='name', memory_key='chat_history')
dob_memory = ConversationBufferMemory(input_key='person', memory_key='chat_history')
facts_memory = ConversationBufferMemory(input_key='dob', memory_key='facts_history')

chain = LLMChain(llm=llm,
                 prompt=first_input, 
                 verbose=True, 
                 output_key='person', 
                 memory=person_memory)

second_input = PromptTemplate(
    input_variables = ['person'],
    template = """
    When was {person} born
    """
)

chain_2 = LLMChain(llm=llm,
                   prompt=second_input, 
                   verbose=True, 
                   output_key='dob',
                   memory=dob_memory)

third_input = PromptTemplate(
    input_variables = ['dob'],
    template = """
    Mention 5 major highlights around {dob} in the world.
    """
)

chain_3 = LLMChain(llm=llm,
                   prompt=third_input, 
                   verbose=True, 
                   output_key='facts',
                   memory=facts_memory)


# Returns the fianl answer at the downstrem of the chains.
parent_chain = SimpleSequentialChain(chains=[chain, chain_2], verbose=True)

paretn_chain_longAnswer = SequentialChain(chains=[chain, chain_2, chain_3], 
                                          input_variables=['name'],
                                          output_variables=['person', 'dob', 'facts'],
                                          verbose=True)

if input_text:
    
    # st.write(parent_chain.run(input_text))
    
    # st.write(paretn_chain_longAnswer({'name':input_text}))

    st.write(paretn_chain_longAnswer({'name':input_text}))

    with st.expander('Person Name'): 
        st.info(person_memory.buffer)

    with st.expander('Major Events'): 
        st.info(facts_memory.buffer)