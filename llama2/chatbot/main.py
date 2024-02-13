
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain_community.llms import Replicate

import streamlit as st
import os

from app import memory_handeling

# Title of the application
st.title('AI-Based Conversational Chatbot')

# Using columns to create a two-panel layout similar to the sketch
col1, col2 = st.columns(2)

with col1:
    st.header('Inputs')
    
    # Model selection dropdown with an option for a custom model
    model_options = {
        'Llama2_7b': 'meta/llama-2-7b-chat:13c3cdee13ee059ab779f0291d29054dab00a47dad8261375654de5540165fb0',
        'Llama2_13b': 'meta/llama-2-13b-chat:f4e2de70d66816a838a89eeeb621910adffb0dd0baba3976c96980970978018d',
        'Llama2_70b': 'meta/llama-2-70b-chat:02e509c789964a7ea8736978a43525956ef40397be9033abf9fd2badfe68c9e3',
        'Mixtral_7b': 'mistralai/mistral-7b-v0.1:3ab1d218053dab642ffd4608fcaa4a864cae1d4a9c5dde7b7db939e8af3767af',
        'Google T5 XL': 'replicate/flan-t5-xl:7a216605843d87f5426a10d2cc6940485a232336ed04d655ef86b91e020e9210',
        'custom': 'custom'
    }
    
    model_display_names = list(model_options.keys())
    model_choice = st.selectbox(
        'Choose your Model:',
        model_display_names
    )

    # Conditional input that appears if the user selects "custom"
    # Get the actual model identifier from the model options dictionary
    llm_model = model_options[model_choice]

    # Conditional input for custom model URL
    if llm_model == 'custom':
        custom_model_url = st.text_input('Enter Your Desired Model Version from Replicate:')
    
    # Subtext for model selection
    st.caption('Select your desired model from [Replicate](https://replicate.com/collections/language-models)')

    # Prompt text area
    prompt_text = st.text_area('Prompt:', height=150)
    prompt_text = prompt_text.lower()
    st.caption('Write "exit" to finish the chat.')

    # Define assistant roles with a default and a custom option
    assistant_roles = [
        'A Respectful Honest Assistant', 
        'A Friendly Assistant', 
        'A Professional Assistant', 
        'custom'
    ]

    # Assistant role selection with a default value
    role_choice = st.selectbox(
        'Assistant Role:',
        assistant_roles,
        index=0  # Default value is the first option
    )
    st.caption('For more on this, see this [Huggingface Models](https://huggingface.co/models)')

    # Conditional input for custom role
    if role_choice == 'custom':
        custom_role = st.text_input('Define your custom assistant role:')

    relo_model = custom_role if role_choice == 'custom' else role_choice

    # Define repo id for tekinazation and a custom option
    repo_id = [
        'mistralai/Mixtral-8x7B-v0.1', 
        'custom'
    ]
    repo_id_choice = st.selectbox(
        'Repo ID for Counting the Tokens:',
        repo_id,
        index=0  # Default value is the first option
    )

    # Conditional input for custom role
    if repo_id_choice == 'custom':
        custom_repo_id = st.text_input('Define your custom repo id:')

    # The actual role variable used in the app will be set based on the user's choice
    repo_id_model = custom_repo_id if role_choice == 'custom' else repo_id_choice

    # Maximum number of tokens to generate
    max_tokens = st.number_input('Max New Token:', min_value=1, value=500, step=1)

    # Subtext for max_tokens
    st.caption('Maximum number of tokens to generate. Note that a word is generally 2-3 tokens.')
    st.caption('For more on this, see this Huggingface [Forum](https://discuss.huggingface.co/t/question-about-maximum-number-of-tokens/3544/2)')

    # Temperature setting
    temperature = st.slider('Temperature:', min_value=0.0, max_value=1.0, value=0.75, step=0.1)
    st.caption("A hyperparameter that regulates the randomness, or creativity, of the AI's responses. Temperature of 1 is random and 0 is deterministic.")
    st.caption('For more on this see this [article](https://medium.com/@amansinghalml_33304/temperature-llms-b41d75870510)')

    # Top-p setting
    top_p = st.slider('Top-p:', min_value=0.0, max_value=1.0, value=0.8, step=0.1)
    st.caption("Controls the model output by augmenting the vocabulary size as only those tokens are considered for which the cumulative probability is greater than the top_p value ")
    st.caption('For more on this see this [article](https://medium.com/@dixnjakindah/top-p-temperature-and-other-parameters-1a53d2f8d7d7)')

    replicate_api_key = st.text_input(
        "Replicate API Key",
        type="password",
        help="Enter your API key for HuggingFace Hub."
    )
    
    st.markdown(
        "[Get a Replicate API key](https://replicate.com/)"
    )
    st.markdown("[View the source code](https://github.com/reabdi/llms/tree/dev/llama2/chatbot)"
    )

    run_button = st.button('Run')


with col2:
    st.header('Outputs')

    # Key names for session state
    REPLICATE_KEY = "replicate_api_token"
    CHAT_LLM_KEY = "chat_llm"
    CONVERSATION_KEY = "conversation"

    # Initialize the output area for the chatbot's answer
    answer_placeholder = st.empty()
    #token_count_placeholder = st.empty()

    # When the run button is clicked
    if run_button:
        if not replicate_api_key:
            st.error("Please add your Replicate API key to continue.")
            st.stop() 
        else:
            # Check and set Replicate API token environment variable
            if REPLICATE_KEY not in st.session_state:
                st.session_state[REPLICATE_KEY] = replicate_api_key
                os.environ["REPLICATE_API_TOKEN"] = st.session_state[REPLICATE_KEY]
            # Initialize Replicate and ConversationChain only if not already done
            if CHAT_LLM_KEY not in st.session_state or CONVERSATION_KEY not in st.session_state:
                st.session_state[CHAT_LLM_KEY] = Replicate(
                    model=llm_model,
                    model_kwargs={"temperature": temperature, "top_p": top_p, "max_new_tokens": max_tokens}
                )
                st.session_state[CONVERSATION_KEY] = ConversationChain(
                    llm=st.session_state[CHAT_LLM_KEY],
                    verbose=True,
                    memory=ConversationBufferMemory()
                )
            # Show a message while loading the response
            with st.spinner("Generating the answer..."):
                try:
                    # Use the objects from session state
                    chat_llm = st.session_state[CHAT_LLM_KEY]
                    conversation = st.session_state[CONVERSATION_KEY]
                    (response, num_tokens, conversation_total_tokens, history) = memory_handeling(
                        prompt_text, relo_model, repo_id_model, conversation, chat_llm
                    )
                    st.success("Response generated successfully!")
                except Exception as e:
                    st.error(f"An error occurred: {e}")
                    st.stop()               
            if prompt_text == 'exit':
                st.error(f"{conversation_total_tokens} tokens used in total in this conversation")
                st.stop()
            # Update the text areas with the response and token count
            answer_placeholder.text_area('Answer:', value=response, height=150)
            st.subheader("Token Count Sent Is:")
            st.write(num_tokens)
            with st.expander("Chat History"):
                st.write(history)

