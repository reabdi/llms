# Google Gemini-Pro Chatbot
**Goal:** 
The goal of this model is to create an LLm based chatbot using Google Gemini Pro 

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

**2. Creating the .env file and creating the *GOOGLE_API_KEY***

visit here: https://ai.google.dev/

**3. Installing the requirements from the requirement.txt**\
List of packages
* streamlit
* google-generativeai

To install the packages:
* **Mac**
    ```bash
    pip3 install -r requirements.txt
    ```
* **Windows**
    ```bash
    pip install -r requirements.txt
    ```

**4. The next step is to create the application using the installed packages.**
Check the application.py files for the source code.

Run the following line and provide the inputs to get the results.

```bash
streamlit run application.py
```
