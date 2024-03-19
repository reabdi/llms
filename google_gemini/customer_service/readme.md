


# LLM-Based Memory-Enabled Chatbot
**Goal:** 


The overall goal of this code is to automate the processing and analysis of customer inquiries using advanced NLP models, enabling efficient categorization, sentiment analysis, and priority assessment to improve customer service and support decision-making.

## Steps to follow:

**1. Creating the environment:**

* **Mac**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```
* **Windows**
    ```bash
    python -m venv .venv
    .\venv\Scripts\activate
    ```

**2. Getting the *REPLICATE_API_TOKRN***

visit here: https://replicate.com/account/api-tokens

**3. Installing the requirements from the requirement.txt**\
List of packages
* langchain
* langchain_core
* langchain-google-genai
* langchain_experimental
* google-generativeai==0.3.1
* google-ai-generativelanguage==0.4.0
* streamlit
* python-dotenv

To install the packages:
* **Mac**
    ```bash
    pip3 install -r requirements.txt
    ```
* **Windows**
    ```bash
    pip install -r requirements.txt
    ```
**4. The next step is creatiging the application using the installed packages.**
Note: Check the application.py for the code.

**5. After finishing the code, the final step is to run the Streamlit:**
```bash
streamlit run main.py
```

**6. Code explanation:**

This code represents a comprehensive customer inquiry processing and analysis application designed for data scientists and ML engineers, leveraging Google's Generative AI capabilities. It is structured into two main parts: information extraction and post-processing of the extracted information.

The first part, info_extractor, uses the Google Generative AI model, specifically "gemini-pro," to classify customer inquiries into predefined categories (e.g., error, updates, maintenance) and extract critical information from these inquiries, such as the customer's full name, company, contact details, and the main request. This function dynamically generates a prompt based on the input message and additional category classes, processes the message using a large language model (LLM) chain, and returns a structured JSON response containing the extracted information.

The second part, post_processing_llm, further processes the extracted information. It categorizes the sentiment of the inquiry into positive, negative, or neutral, determines the priority level (high, medium, low) based on the request's content, and provides insights into any errors mentioned in the inquiry by summarizing potential causes found on the web. This step aims to refine the raw output from the information extraction process, making it more actionable for customer service or sales teams.

The Streamlit application (main.py) serves as the user interface for this processing pipeline. It allows users to upload files containing customer inquiries, input their Google API key for accessing the Gemini model, and run the analysis. The application aggregates the processed inquiries, generates a summary table of the analysis (total calls, sentiment analysis, priority levels), and offers the option to download the aggregated results as a CSV file.


Here is a screnshot of the UI:

<img width="635" alt="Screenshot 2024-03-18 at 10 28 38 PM" src="https://github.com/reabdi/llms/assets/45298432/92c5e45b-7ce5-4fd1-bf70-bb4e46a6db21">



