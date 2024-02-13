from langchain_community.llms import Replicate
from langchain.schema.messages import get_buffer_string
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from transformers import AutoTokenizer

from typing import Dict, List
import os

def memory_handeling(prompt_text, role, repo_id, conversation, chat_llm):
    conversation_total_tokens = 0
    tokenizer = AutoTokenizer.from_pretrained(repo_id)  
    new_conversation = ConversationChain(llm=chat_llm, 
                                    verbose=False, 
                                    memory=ConversationBufferMemory()
                                    )
    message = f"""
                You are a {role} and you need to answer the following question. 
                {prompt_text}
                Keep your answers short and to the point.
                """

    formatted_prompt = conversation.prompt.format(input=message,history=new_conversation.memory.buffer)
    num_tokens = len(tokenizer.tokenize(formatted_prompt))
    conversation_total_tokens += num_tokens
    #print(f'tokens sent {num_tokens}')
    response = conversation.predict(input=formatted_prompt)
    response_num_tokens = len(tokenizer.tokenize(response))
    conversation_total_tokens += response_num_tokens
    #print(f"LLM: {response}")

    return (response, num_tokens, conversation_total_tokens, conversation.memory.buffer)