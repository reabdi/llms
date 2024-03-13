
import os
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_experimental.agents import create_csv_agent

# Loading environment variables
from dotenv import (
    load_dotenv,
)  
load_dotenv() 

genai.configure(
    api_key=os.getenv("GOOGLE_API_KEY")
)

def info_extractor(message):
    llm = ChatGoogleGenerativeAI(model="gemini-pro",
                             temperature=0.)
    
    agent = create_csv_agent(llm, 
                         'csv_file/hashed_wab_reviews.csv', 
                         verbose=True)

    response = agent.run(message)
    return response

if __name__ == "__main__":
    # message = "how many rows are there?"
    # message = "From how many distinct countary we have data?"
    
    answer = info_extractor(message)
    print(answer)