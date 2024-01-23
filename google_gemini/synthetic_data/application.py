# Importing necessary libraries and modules
import google.generativeai as genai  # Google's generative AI library


# Define a function to get response from Gemini model
def get_gimini_response(datamodel, constraints_items, recordsNumber):
    # Generating content using the Gemini model
    prompt_template = f"""
    You are an expert in generating synthetic datasets based on the data schema, the provided constraints, and number of desired records you're getting by.
    The data schema, the contraints on the some or all the variables, as well as the number of the synthetic records requedted will be provide in this prompt and you should generate synthetic data in JSON format. 
    Make sure to generate the synthetic data exactly based on the format provide as the checks in the datamodel structure and infoamtion you're getting from constraints.

    The dataset schema specifies the following key details as a SQL code:{datamodel} 

    The constrainsts thas should be considered in creating the synthertic data:{constraints_items}

    The number of records that is needed to be genreated:{recordsNumber}

    Based on the guidelines, generate a diverse and representative set of synthetic data. 
    Ensure that the data adheres closely to the described schema, maintaining consistency in data types and respecting all constraints and patterns. 
    The output should be in JSON format, with each row representing a separate record following the schema's structure."
    """
    # Initialize the Google Gemini Pro Vision model
    model = genai.GenerativeModel("gemini-pro")  # Load the Gemini Pro model
    response = model.generate_content(
        prompt_template
    )  # Generate response based on input, data model (text), and prompt
    return response.text  # Return the textual part of the response

