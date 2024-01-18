# Multi Language Invoice Extracter
**Goal:** 
This model is to create an AI based (Here Google Gemini) tool to extract text from PDF files.

## Steps to follow:

**1. Creating the environment:**
```bash
conda create -p venv python==3.10 -y
conda activate venv/
```
**2. Creatign the env file and providing the *GOOGLE_API_KEY***
vist here: https://ai.google.dev/

**3. Installing the requirement from the requirement.txt**
* streamlit
* google-generativeai

```bash
pip install watchdog
pip install -r requirements.txt
```

**4. The next step is creatiging the application using the installed packages.**
Note: Check the application.py for the code.

**5. After finishing the code, the final step is to run the Streamlit:**
```bash
streamlit run application.py
```

Sample Interface:
![Screenshot 2024-01-17 at 11 28 35 PM](https://github.com/reabdi/llms/assets/45298432/6f7e4af6-08ac-4f53-825d-d3eea613e7ad)



Sample Prompts could be:
- Who is this invoice billed to?
- Tell me how much was deposit requested?
- What is the final amount due?
- What is the date of the invoice?
