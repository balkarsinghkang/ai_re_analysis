import json
from jinja2 import Template

def build_prompt(template_path="prompts/underwriting_prompt.txt", property_data=None):
    # Load the prompt template
    with open(template_path, "r") as file:
        template_text = file.read()

    # Create Jinja2 template
    template = Template(template_text)

    # Handle missing data by providing default values
    for key, value in property_data.items():
        if value is None or value == "":
            property_data[key] = "N/A"  # Default value for missing fields

    # Fill the template with data
    filled_prompt = template.render(**property_data)

    return filled_prompt
