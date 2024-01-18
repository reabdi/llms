import google.generativeai as genai
import streamlit as st
from PIL import Image

import os

from dotenv import load_dotenv
load_dotenv()

# Confiduring the Gemini model
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load the Google Gemini Pro Vision
model = genai.GenerativeModel('gemini-pro-vision')

def get_gimini_response(input, image, prompt):
    response=model.generate_content([input, image[0], prompt])
    return response.text

# Function to display the uploaded image
def input_image_details(uploaded_file):
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,    # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No File Uploaded...")

# The Streamlit UI setup
st.set_page_config(page_title="Multi-Language Invoice Extractor")

st.header("Multi-Language Invoice Extractor")
input=st.text_input("Input Prompt: ", key="Input")
uploaded_file=st.file_uploader("Choose an image for the desired invoice...:", type=["jpg", "jpeg", "png"])

image=""
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit=st.button("Tell me about the invoice...")

input_prompt="""
You are an expert in understanding the invoices based on images and files you're getting to analyze.
The user will uploaded an image as the invoice and you should answer to any questions based on the uploaded invoice image.
"""

# If submit button is clicked
if submit:
    image_data = input_image_details(uploaded_file)
    response = get_gimini_response(input_prompt, image_data, input)
    st.subheader("The response is...")
    st.write(response)