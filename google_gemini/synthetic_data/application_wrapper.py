# Importing necessary libraries and modules
import google.generativeai as genai  # Google's generative AI library
import streamlit as st  # Streamlit library for creating web apps
import os  # Standard library for OS interface
import json

# Loading environment variables
from dotenv import (
    load_dotenv,
)  # Dotenv for loading environment variables from a .env file

load_dotenv()  # Load environment variables from .env file

# Configuring the Gemini model with an API key
genai.configure(
    api_key=os.getenv("GOOGLE_API_KEY")
)  # Set the API key for the Gemini model

# Initialize the Google Gemini Pro Vision model
model = genai.GenerativeModel('gemini-pro')  # Load the Gemini Pro model


# Define a function to get response from Gemini model
def get_gimini_response(data_model, constraints_items, recordsNumber):
    # Generating content using the Gemini model
    prompt_template = f"""
    You are an expert in generating synthetic datasets based on the data schema, the provided constraints, and number of desired records you're getting by.
    The data schema, the contraints on the some or all the variables, as well as the number of the synthetic records requedted will be provide in this prompt and you should generate synthetic data in JSON format. 
    Make sure to generate the synthetic data exactly based on the format provide as the checks in the datamodel structure and infoamtion you're getting from constraints.

    The dataset schema specifies the following key details as a SQL code:{data_model} 

    You should provide data for all the variabels in the data_model,
    Also you should consider the constrainsts in creating the data for the following columns:{constraints_items}

    The number of records that is needed to be genreated:{recordsNumber}

    Based on the guidelines, generate a diverse and representative set of synthetic data. 
    Ensure that the data adheres closely to the described schema, maintaining consistency in data types and respecting all constraints and patterns. 
    The output should be in JSON format, with each row representing a separate record following the schema's structure."
    """

    response = model.generate_content(
        prompt_template
    )  # Generate response based on input, data model (text), and prompt
    return response.text  # Return the textual part of the response

 
# Define the function to read the file
def read_file(file_path):
    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return
    try:
        # Open the file using 'with' statement for safe handling
        with open(file_path, 'r', encoding='utf-8') as file:
            # Read the contents of the file
            contents = file.read()
        return contents
    except IOError as e:
        # Handle any IO errors
        print(f"Error reading file: {e}")

# Function to write JSON data to a file in the current directory
def write_json_to_file(data, filename):
    try:
        # Open the file and write the JSON data
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
        print(f"Data written to {filename}")
    except IOError as e:
        # Handle file I/O errors
        print(f"Error writing to file: {e}")

if __name__ == "__main__":

    # List of constraints
    """
    example:
    1) Create some repetitive values for User_Id. 
    2) Job_Id and Reference_Job_Id should be the value, 
    3) Use UTC format for Activity_Timestamp, ds, and ts
    """
    constraints_list = """

    """

    # User input for number of records
    num_records = 5

    # User input for number of runs of the wrapper
    num_runs = 5

    file_path = "sample_schema/schema.txt"

    string_data =  read_file(file_path)
    
    response = get_gimini_response(
        string_data, constraints_list, num_records
    )

    # json_string = response.strip("```json").strip("```").strip()
    # #print(json_string)
    # file_name = 'synthetic_data_sample.json'
    # with open(file_name, "w") as f:
    #     f.write(json_string)

    # Initialize an empty list to aggregate results
    aggregated_data = []
    # Example: run the function 5 times
    for _ in range(num_runs):
        json_output = get_gimini_response(
        string_data, constraints_list, num_records
        )
        json_string = response.strip("```json").strip("```").strip()
        # Append the data from this run to the aggregated list
        aggregated_data.extend(json.loads(json_string))

    # Convert the aggregated data back to JSON string
    final_json_string = json.dumps(aggregated_data, indent=4)

    #print(final_json_string)

    # Write the final JSON string to a file
    with open('final_output.json', 'w') as file:
        file.write(final_json_string)


