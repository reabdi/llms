import os
import json
import ast
import google.generativeai as genai
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import Tool
from langchain_community.utilities import SerpAPIWrapper
from langchain.agents import initialize_agent


# Loading environment variables
from dotenv import (
    load_dotenv,
)  
load_dotenv() 

# Configuring the Gemini model with an API key
genai.configure(
    api_key=os.getenv("GOOGLE_API_KEY")
)


def info_extractor(message):

    llm = ChatGoogleGenerativeAI(model="gemini-pro",
                             temperature=0.)
    
    category_classes = """
        1. "error" if the message is asking or reporting a problem or error in the software.
        2. "updates" for any inquery about software updates and upcoming modules
        3. "maintenance" for any request for maintenance scheduleidng witht the company
        4. "licencing" for any inquery about the software licence
        5. "sales" for any question about the prices, costs, sales, payment methods and other financial related issues. 
        You may found multiple categories from messags, make sure you provide all as a list. 
    """
    
    infoExtractor_prompt = PromptTemplate.from_template(
    """You are a business communication expert.
            Extract the following infoamtion from:\n\n {_message} 
            The full name as "full_name"
            The company as "company"
            The phone number as "phone_number"
            The email address as "email"
            The full address as "address"
            The city as "city"
            The state as "state"
            The zipcode as "zipcode"
            The main request, asked by the person as "request"
            The sentiment you're getting from the message as "sentiment". This can be positive, negative, or neutral.
            The categories of the request based on this additional information: {_category_classes}
            Anything else you thing would be usedul for the custoemr service. \n\n
            Then I want you then to create a json format based on this infoamtion. Do not include anything else, just the the json as a string format. 
            Note that if you couldn't find the determined infaomtion from message, use null value instead.
            """
    )

    extract_chain = LLMChain(llm=llm, prompt=infoExtractor_prompt)

    response = extract_chain.run({"_message":message, "_category_classes":category_classes})
    #return json.loads(response.strip('` \n'))
    return response


def post_processing_llm(row_response):

    llm = ChatGoogleGenerativeAI(model="gemini-pro",
                             temperature=0.)

    # Promt for post processing:
    list_names = "sentiment_positive, sentiment_negative, sentiment_neutral"
    list_priority = "priority_high, priority_medium, priority_low"

    post_processing_prompt = PromptTemplate.from_template("""You are a python progremmer and business communication expert.
            You're getting the following string which has structure similar to a python dictionary: {_row_response} \n
            Based on the input dictionary, create a new dictionary and follow the next steps to complete the prompt.
            Begin! \n
            key: "content", variable: consider the python dictionary you have received. Do not include any other characters to the dictrionary.\n
            key: "sentiment", variable: select an apprpriate value only from this list: {_list_names}, based on the 'sentiment' in the input dictionary.\n
            key: "priority", variable: create a priority variable by selecting an apprpriate name only from this list of names: {_list_priority}, based on the 'request' in the outcome input dictioanry.\n
            key: "error", variable: only if you see "error" as a value for the 'categories' in the input dictionary, seacrh the web to find some possible reasosns but provide a short summary of what you find. If there's no "error" put None.\n 
            Return the results only as a pyhton dictioanry. Return nothin more. Let's think step by step.\n  
        """
    )

    extract_chain = LLMChain(llm=llm, prompt=post_processing_prompt)

    response = extract_chain.run({"_row_response":row_response, "_list_names":list_names, "_list_priority":list_priority})
    return response