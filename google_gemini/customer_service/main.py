import streamlit as st
import os
import ast
import time
import pandas as pd

from app import info_extractor, post_processing_llm


def output_generator(result_dict, aggregated_list):
    result_dict['content']['sentiment_category'] = result_dict["sentiment"]
    result_dict['content']['priority'] = result_dict['priority']
    result_dict['content']['insights'] = result_dict['error']
    
    aggregated_list.append(result_dict['content'])

def summary_table_generator(df_data):

    total_summary = [
        {"Discription": "Total # of calls", "Number": len(df_data)},
        {"Discription": "Total # of unique caller", "Number": df_data['full_name'].nunique()},
        {"Discription": "Total # positive sentiment", "Number": len(df_data[df_data['sentiment_category'].isin(["sentiment_positive", 'positive'])])},
        {"Discription": "Total # negative sentiment", "Number": len(df_data[df_data['sentiment_category'].isin(["sentiment_negative", 'negative'])])},
        {"Discription": "Total # neutral sentiment", "Number": len(df_data[df_data['sentiment_category'].isin(["sentiment_neutral", 'neutral'])])},
        {"Discription": "Total # high priority", "Number": len(df_data[df_data['priority'].isin(["priority_high", 'high'])])},
        {"Discription": "Total # medium priority", "Number": len(df_data[df_data['priority'].isin(["priority_medium", 'medium'])])},
        {"Discription": "Total # low priority", "Number": len(df_data[df_data['priority'].isin(["priority_low", 'low'])])}
    ]
    # Convert the list of dictionaries into a pandas DataFrame
    return pd.DataFrame(total_summary)

# Logo at the top of the application
st.image("image/inqlect_logo.webp", width=180) 

# Title of the application
st.title('INQLECT')
st.caption('Get AI-Powered Inquiry Intellect')
st.markdown("---") 

# Using columns to create a two-panel layout similar to the sketch
col1, col2 = st.columns(2)

with col1:
    st.header('Inputs')
    # Create a file uploader widget
    uploaded_files = st.file_uploader("Choose files:", accept_multiple_files=True)
    
    # Display the names of the uploaded files
    # for uploaded_file in uploaded_files:
    #     st.write(uploaded_file.name)

    google_api_key = st.text_input(
        "Gemini API Key",
        type="password",
        help="Enter your Google API key."
    )

    st.markdown(
        "[Get a Google API key](https://ai.google.dev/)"
    )

    st.markdown("[View the source code](https://github.com/reabdi/llms/tree/main/google_gemini/customer_service)"
    )

    run_button = st.button('Run')

    st.markdown("***")
    st.markdown("Powered by [Google Gemini](https://gemini.google.com/app)")


with col2:
    st.header('Outputs')

    # Key names for session state
    GOOGLE_API_KEY = "google_api_key"
    # When the run button is clicked
    if run_button:
        if not google_api_key:
            st.error("Please add your API key to continue.")
            st.stop()
        else:
            # Check and set API token environment variables
            if GOOGLE_API_KEY not in st.session_state:
                st.session_state[GOOGLE_API_KEY] = google_api_key
                os.environ["google_api_key"] = st.session_state[GOOGLE_API_KEY]
            
            aggregated_data = []
            # Show a message while loading the response
            with st.spinner("Generating the answer..."):
                try:
                    message_placeholder = st.empty()  # Create a placeholder for the temporary message
                    
                    for uploaded_file in uploaded_files:
                        # Initialize session state for message display
                        if 'display_message' not in st.session_state:
                            st.session_state.display_message = True
                        content = uploaded_file.getvalue().decode('utf-8')
                        response = info_extractor(content)
                        post_results = post_processing_llm(response)
                        dict_string = post_results.strip('`python\n')
                        # Replace 'null' with 'None' to make it a valid Python dictionary string
                        dict_string = dict_string.replace('null', 'None')
                        # Convert the string representation of the dictionary to an actual Python dictionary
                        actual_dict = ast.literal_eval(dict_string)
                        output_generator(actual_dict, aggregated_data)

                        if 'message_display_time' not in st.session_state or time.time() - st.session_state.message_display_time > 5:
                            st.session_state.message_display_time = time.time()
                            message_placeholder.info(f"Response generated successfully for {actual_dict['content']['full_name']}...")

                        # Clear the message after a delay
                        if time.time() - st.session_state.message_display_time <= 5:
                            time.sleep(5 - (time.time() - st.session_state.message_display_time))  # Adjust sleep to ensure a total of 5 seconds display
                            message_placeholder.empty()  # Clear the temporary message
                    st.success("Response generated successfully for all users!")
                    # Convert the aggregated results into a DataFrame
                    df_aggregated_data = pd.DataFrame(aggregated_data)
                    # Convert the DataFrame to a CSV string
                    csv_aggregated_data = df_aggregated_data.to_csv(index=True)
                except Exception as e:
                    st.error(f"An error occurred: {e}")
                    st.stop()
            # Providing a summary for the user:
            df_summary = summary_table_generator(df_aggregated_data)
            st.dataframe(df_summary)
            # Display the downloadable generated data in an expander
            with st.expander("Generated Data:"):
                # Create a download button and provide the CSV string as the file to download
                st.download_button(
                    label="Download Aggregated Results as CSV",
                    data=csv_aggregated_data,
                    file_name="aggregated_results.csv",
                    mime="text/csv",
                )
