# Synthetic Data Generator
**Goal:** 
The goal of this model is to create an LLm based tool using Google Gemini Pro to create synthetic data based on the desired data model. 

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

**4. The next step is to create the application using the installed packages.**
Check the application.py and application_wrapper.py files for the code.

The tool includes two python files:

The **application.py** and **main.py** files that include the code that is needed for running the Streamlit web application.\
To that end run the following line and provide the inputs to get the results.

```bash
streamlit run main.py
```

# Running the app by a Python Wrapper
Due to the limitation in number of tokents the Google Gemini Pro generating in its responses, there's a chance taht the user wouldn't be able to get the desired number of data points. In order to solve this issue, a pyhton-based wrapper can be used which is avialble in **applicaiton_wrapper.py**.

The user should determie:
* The path to the input schema (text file)
* The possible constrained that should be considered by the model in the pyhton code
* The number of data points for each run
* The number of runs for the wrapper
* The file name and address for the final output

Then, the final JSON file will be created based on the input data. Besides the wrapper, the straucture of both files is identical.

* **Mac**
    ```bash
    python3 application_wrapper.py
    ```
* **Windows**
    ```bash
    python application_wrapper.py
    ```

**NOTE:** Sample inputs and outputs are availabe [HERE](sample_schema/schema_1.txt)

Sample Interface:
<img width="1308" alt="Screenshot 2024-01-23 at 12 22 15 AM" src="https://github.com/reabdi/llms/assets/45298432/99f037b2-cd00-42ca-bc7a-8326e428f7c7">