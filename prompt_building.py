import json
from jinja2 import Template

def build_prompt(template_path="prompts/underwriting_prompt.txt", data_path="input.json"):
    # Load the prompt template
    with open(template_path, "r") as file:
        template_text = file.read()

    # Create Jinja2 template
    template = Template(template_text)

    # Load property data from input.json
    with open(data_path, "r") as json_file:
        property_data = json.load(json_file)

    # Handle missing data by providing default values
    for key, value in property_data.items():
        if value is None:
            property_data[key] = "N/A"  # Default value for missing fields

    # Fill the template with data
    filled_prompt = template.render(**property_data)

    return filled_prompt
