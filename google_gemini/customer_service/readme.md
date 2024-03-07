# LLM-Based Memory-Enabled Chatbot
**Goal:** 
TBD

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
