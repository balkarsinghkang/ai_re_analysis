from flask import Flask, render_template, request
import os
from prompt_building import build_prompt
# import openai  # Import the OpenAI module to resolve the NameError
from openai import OpenAI
# Initialize Flask app
app = Flask(__name__)

# Read API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("The environment variable 'OPENAI_API_KEY' is not set.")

# openai.api_key = api_key
client = OpenAI(api_key=api_key)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    # Get property details from the form
    property_details = request.form.to_dict()

    # Generate the filled prompt using the property details
    filled_prompt = build_prompt(property_data=property_details)

    # Use the filled prompt in the OpenAI API call
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a real estate underwriter."},
            {"role": "user", "content": filled_prompt}
        ],
        temperature=0.2  # Low temperature for more factual outputs
    )

    # Extract the content from the response
    analysis_output = response.choices[0].message.content

    # Return the analysis output to the webpage
    return render_template('index.html', analysis_output=analysis_output)

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Debugging enabled
