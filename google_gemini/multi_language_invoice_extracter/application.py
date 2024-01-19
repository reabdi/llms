# Importing necessary libraries and modules
import google.generativeai as genai  # Google's generative AI library
import streamlit as st  # Streamlit library for creating web apps

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
model = genai.GenerativeModel("gemini-pro-vision")  # Load the Gemini Pro Vision model


# Define a function to get response from Gemini model
def get_gimini_response(input, image, prompt):
    # Generating content using the Gemini model
    response = model.generate_content(
        [input, image[0], prompt]
    )  # Generate response based on input, image, and prompt
    return response.text  # Return the textual part of the response


# Define a function to process the uploaded image
def input_image_details(uploaded_file):
    if uploaded_file is not None:
        # Convert uploaded file into bytes
        bytes_data = uploaded_file.getvalue()  # Read file as byte data

        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Extract MIME type of the file
                "data": bytes_data,  # Include byte data of the image
            }
        ]
        return image_parts
    else:
        # Error handling if no file is uploaded
        raise FileNotFoundError("No File Uploaded...")


# Setting up the Streamlit user interface
st.set_page_config(
    page_title="Multi-Language Invoice Extractor"
)  # Configuring Streamlit page

# Creating Streamlit UI components
st.header("Multi-Language Invoice Extractor")  # Page header
input = st.text_input("Input Prompt: ", key="Input")  # Input text box for user prompt
uploaded_file = st.file_uploader(
    "Choose an image for the desired invoice...:", type=["jpg", "jpeg", "png"]
)  # File uploader

image = ""
if uploaded_file is not None:
    # Displaying the uploaded image
    image = Image.open(uploaded_file)  # Open the uploaded image file
    st.image(
        image, caption="Uploaded Image.", use_column_width=True
    )  # Display the image in Streamlit app

submit = st.button("Tell me about the invoice...")  # Submit button

# Predefined input prompt for the Gemini model
input_prompt = """
You are an expert in understanding the invoices based on images and files you're getting to analyze.
The user will upload an image as the invoice and you should answer any questions based on the uploaded invoice image.
"""

# Handling the submit action
if submit:
    image_data = input_image_details(uploaded_file)  # Process the uploaded image
    response = get_gimini_response(
        input_prompt, image_data, input
    )  # Get response from the Gemini model
    st.subheader("The response is...")  # Display subheader
    st.write(response)  # Show the response in the Streamlit app
