import json


def load_data(file_path):
    """Loads a JSON file and returns its content"""
    with open(file_path, "r") as handle:
        return json.load(handle)


def serialize_animal(animal):
    """Convert a single animal object into an HTML list item"""
    output = '<li class="cards__item">\n'

    # Title (animal name)
    if "name" in animal:
        output += f'  <div class="card__title">{animal["name"]}</div>\n'

    # Body (diet, location, type)
    output += '  <p class="card__text">\n'
    if "characteristics" in animal and "diet" in animal["characteristics"]:
        output += f'      <strong>Diet:</strong> {animal["characteristics"]["diet"]}<br/>\n'
    if "locations" in animal and len(animal["locations"]) > 0:
        output += f'      <strong>Location:</strong> {animal["locations"][0]}<br/>\n'
    if "characteristics" in animal and "type" in animal["characteristics"]:
        output += f'      <strong>Type:</strong> {animal["characteristics"]["type"]}<br/>\n'
    output += "  </p>\n"

    output += "</li>\n"
    return output


# Step 1: Load data
animals_data = load_data("animals_data.json")

# Step 2: Generate HTML for all animals
output = ""
for animal in animals_data:
    output += serialize_animal(animal)

# Step 3: Read the HTML template
with open("animals_template.html", "r") as file:
    template = file.read()

# Step 4: Replace placeholder with animal info
html_content = template.replace("__REPLACE_ANIMALS_INFO__", output)

# Step 5: Write the final animals.html file
with open("animals.html", "w") as file:
    file.write(html_content)

print("✅ animals.html generated! Open it in your browser.")
