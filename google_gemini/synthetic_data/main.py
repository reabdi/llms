
import google.generativeai as genai  # Google's generative AI library
import streamlit as st
import io

from application import get_gimini_response

# Configure the Streamlit page
st.set_page_config(page_title="Synthetic Data Generator", layout="wide")

# Use a container for page content to improve layout and spacing
with st.container():
    st.title("Synthetic Data Generator")

    # Use columns for layout organization
    left_column, right_column = st.columns((2, 1))
    
    with left_column:
        uploaded_file = st.file_uploader(
            "Provide the desired data schema:",
            type="txt",
            help="Upload a .txt file containing the data schema."
        )

        if uploaded_file is not None:
            # Display the content of the file in an expander
            with st.expander("File Content:"):
                text = io.TextIOWrapper(uploaded_file, encoding="utf-8")
                string_data = text.read()
                st.text_area("", string_data, height=250, disabled=True)
        
        constraints_list = st.text_input(
            "Provide the constraints:",
            placeholder="Enter constraints separated by commas",
            help="Specify constraints for data generation."
        )
        
    with right_column:
        st.write("Settings")
        num_records = st.number_input(
            "Number of records for synthetic data",
            min_value=1, value=5, step=1,
            help="Choose how many records to generate."
        )
        
        google_api_key = st.text_input(
            "Gemini-Pro API Key",
            type="password",
            help="Enter your API key for Gemini-Pro."
        )
        
        st.markdown(
            "[Get a Gemini-Pro API key](https://ai.google.dev) | "
            "[View the source code](https://github.com/reabdi/llms/tree/main/google_gemini/synthetic_data)"
        )
        
        submit = st.button("Generate Synthetic Data", help="Click to generate data.")
        
    # Handling the submit action
    if submit:
        if not uploaded_file:
            st.warning("Please upload a data schema file to continue.")
            st.stop()
        elif not google_api_key:
            st.error("Please add your Google Gemini-Pro API key to continue.")
            st.stop()
        else:
            # Show a message while loading the response
            with st.spinner("Generating data..."):
                # Set the API key for the Gemini model
                genai.configure(api_key=google_api_key)
                schema_data = string_data
                try:
                    response = get_gimini_response(
                        schema_data, constraints_list, num_records
                    )
                    st.success("Data generated successfully!")
                except Exception as e:
                    st.error(f"An error occurred: {e}")
                    st.stop()
                    
            # Display the generated data in an expander
            with st.expander("Generated Data:"):
                st.write(response)

# Include a horizontal line and the powered by text
st.markdown(
    """<hr/><p style='text-align:center'>Powered By <a href='https://deepmind.google/technologies/gemini/#introduction' target='_blank'>Google Gemini-Pro</a></p>""",
    unsafe_allow_html=True
)
