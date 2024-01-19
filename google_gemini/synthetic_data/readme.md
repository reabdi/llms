# Synthetic Data Generator
**Goal:** 
The goal of this model is to create an LLm based tool using Google Gemini Pro to create synthetic data based on the desired data model. 

## Steps to follow:

**1. Creating the environment:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**2. Creating the required files for the task**

```bash
touch .env
touch requirements.txt
touch .gitignore
touch application.py
touch readme.md
```

**3. Creating the env file and providing the *GOOGLE_API_KEY***

visit here: https://ai.google.dev/

**4. Updating the .gitignore file**

Including ".env" and ".venv" to the file -if you want to keep the files remotely."

**5. Installing the requirement from the requirement.txt**
* streamlit
* google-generativeai
* python-dotenv

```bash
pip3 install -r requirements.txt
```

**6. The next step is to create the application using the installed packages.**
Check the application.py and application_wrapper.py files for the code.

The tool includes two python files:

The **application.py** file includes the code that is needed for running the Streamlit web application.\
To taht end run the following line and provide the inputs to get the results.

```bash
streamlit run application.py
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

```bash
python3 application_wrapper.py
```

Sample Interface:
![Screenshot 2024-01-18 at 11 22 45 PM](https://github.com/reabdi/llms/assets/45298432/b5a31bdf-cfa3-407f-b81c-19fe2bd21bda)


Note: Sample inputs and outputs are available in the repo. 
