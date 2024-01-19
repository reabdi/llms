# Importing necessary libraries and modules
import google.generativeai as genai  # Google's generative AI library
import streamlit as st  # Streamlit library for creating web apps
import io  # To display the text on the screen
import os  # Standard library for OS interface


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
model = genai.GenerativeModel("gemini-pro")  # Load the Gemini Pro model


# Define a function to get response from Gemini model
def get_gimini_response(datamodel, constraints_items, recordsNumber):
    # Generating content using the Gemini model
    prompt_template = f"""
    You are an expert in generating synthetic datasets based on the data schema, the provided constraints, and number of desired records you're getting by.
    The data schema, the contraints on the some or all the variables, as well as the number of the synthetic records requedted will be provide in this prompt and you should generate synthetic data in JSON format. 
    Make sure to generate the synthetic data exactly based on the format provide as the checks in the datamodel structure and infoamtion you're getting from constraints.

    The dataset schema specifies the following key details as a SQL code:{datamodel} 

    The constrainsts thas should be considered in creating the synthertic data:{constraints_items}

    The number of records that is needed to be genreated:{recordsNumber}

    Based on the guidelines, generate a diverse and representative set of synthetic data. 
    Ensure that the data adheres closely to the described schema, maintaining consistency in data types and respecting all constraints and patterns. 
    The output should be in JSON format, with each row representing a separate record following the schema's structure."
    """
    response = model.generate_content(
        prompt_template
    )  # Generate response based on input, data model (text), and prompt
    return response.text  # Return the textual part of the response


# Setting up the Streamlit user interface
st.set_page_config(page_title="Synthetic Data Generator")  # Configuring Streamlit page

# Creating Streamlit UI components
st.header("Synthetic Data Generator")  # Page header
uploaded_file = st.file_uploader(
    "Provide the desired data schema:", type="txt"
)  # File uploader

string_data = ""
if uploaded_file is not None:
    # Read the content of the file
    text = io.TextIOWrapper(uploaded_file, encoding="utf-8")
    string_data = text.read()
    # Display the content of the file
    st.text("File Content:")
    st.write(string_data)

constraints_list = st.text_input(
    "Provide the constrainsts: ", key="Input"
)  # Input text box for user prompt

# User input for number of records
num_records = st.number_input(
    "Enter the number of records for synthetic data", min_value=1, value=5, step=1
)

submit = st.button("Generate the synthetic data...")  # Submit button

# Handling the submit action
if submit:
    schema_data = string_data
    response = get_gimini_response(
        schema_data, constraints_list, num_records
    )  # Get response from the Gemini model
    st.subheader("The response is...")  # Display subheader
    st.write(response)  # Show the response in the Streamlit app
