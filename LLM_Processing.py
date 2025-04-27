import os
from openai import OpenAI

# Read API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("The environment variable 'OPENAI_API_KEY' is not set.")

client = OpenAI(api_key=api_key)
from prompt_building import build_prompt

# Generate the filled prompt using the build_prompt function
filled_prompt = build_prompt()

# Use the filled prompt in the OpenAI API call

response = client.chat.completions.create(model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a real estate underwriter."},
        {"role": "user", "content": filled_prompt}
    ],
    temperature=0.2  # Low temperature for more factual outputs
)

analysis_output = response.choices[0].message.content

# Return or display on web page
print(analysis_output)
