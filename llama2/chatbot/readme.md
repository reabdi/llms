# LLM-Based Memory-Enabled Chatbot
**Goal:** 
The goal of this model is to create an LLm-based chatbot with the ability to have memory. The user can select an LLM from the following available open source models or a custom model from [Replicate](https://replicate.com/collections/trainable-language-models)
* LLama 7b, 13b, and 70b
* Mixtral 7b
* Google T5 XL

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
* streamlit
* langchain
* Replicate
* transformers

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
Check the app.py file for the source code.

Run the following line and provide the inputs to get the results.

```bash
streamlit run main.py
```
