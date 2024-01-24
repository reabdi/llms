import google.generativeai as genai  # Google's generative AI library
import streamlit as st
# import io
# import os

# # Loading environment variables
# from dotenv import (
#     load_dotenv,
# )  # Dotenv for loading environment variables from a .env file

# load_dotenv()  # Load environment variables from .env file


def get_gemini_response(question, api_key):
    # Initialize the Google Gemini Pro Vision model
    model = genai.GenerativeModel("gemini-pro")  # Load the Gemini Pro model
    # Configuring the Gemini model with an API key
    genai.configure(
        api_key=api_key
    )  # Set the API key for the Gemini model
    chat=model.start_chat(history=[])
    response=chat.send_message(question, stream=False)
    return response


# Configure the Streamlit page
st.set_page_config(page_title="Google Gemini-Pro Chatbot", layout="wide")

# Apply a professional color scheme and typography
st.markdown("""
    <style>
    .main {
        background-color: #3e454f;
        color: #d1cdcd;
    }
    h1 {
        color: #0d6efd;
    }
    .stTextInput, .stButton, .stSelectbox {
        margin-top: 10px;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        background-color: #0d6efd;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# Use a container for page content to improve layout and spacing
with st.container():
    st.header("Gemini-Pro Application")

    # Initialize session state for chat history if it doesn't exist
    if "Chat History" not in st.session_state:
        st.session_state['Chat History'] = []

    # Organize input fields in columns
    col1, col2 = st.columns([2, 1])
    with col1:
        input_question = st.text_input("Provide Your Input:", placeholder="Enter your input", key="input")
    with col2:
        google_api_key = st.text_input("Gemini-Pro API Key", type="password", help="Enter your API key for Gemini-Pro.")
    
    st.markdown("[Get a Gemini-Pro API key](https://ai.google.dev) | [View the source code](https://github.com/reabdi/llms/tree/main/google_gemini)")

    submit = st.button("Ask the question", help="Click to generate data.")

    # Handling the submit action
    if submit and input_question:
        if not google_api_key:
            st.error("Please add your Google Gemini-Pro API key to continue.")
            st.stop()
        else:
            # Show a message while loading the response
            with st.spinner("Generating the answer..."):
                # Set the API key for the Gemini model
                try:
                    response = get_gemini_response(input_question, google_api_key)
                    st.success("Response generated successfully!")
                except Exception as e:
                    st.error(f"An error occurred: {e}")
                    st.stop()

            # Add user query and response to the session history
            st.session_state['Chat History'].append(("You", input_question))
            st.subheader("The Response Is...")
            st.write(response)
            st.session_state['Chat History'].append(("Bot", response))
            # Display the History
            with st.expander("Chat History"):
                for role, text in st.session_state['Chat History']:
                    st.write(f"{role}: {text}")

            


            