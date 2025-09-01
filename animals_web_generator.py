import json

# Step 1: Load the JSON data
def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)

animals_data = load_data("animals_data.json")

# Step 2: Generate a string with animal data
output = ""
for animal in animals_data:
    output += '<li class="cards__item">\n'  # wrap each animal in a styled card

    if "name" in animal:
        output += f"<div class='card__title'>Name: {animal['name']}</div>\n"

    if "characteristics" in animal and "diet" in animal["characteristics"]:
        output += f"<p class='card__text'>Diet: {animal['characteristics']['diet']}</p>\n"

    if "locations" in animal and len(animal["locations"]) > 0:
        output += f"<p class='card__text'>Location: {animal['locations'][0]}</p>\n"

    if "characteristics" in animal and "type" in animal["characteristics"]:
        output += f"<p class='card__text'>Type: {animal['characteristics']['type']}</p>\n"

    output += "</li>\n\n"

# Step 3: Read the HTML template
with open("animals_template.html", "r") as file:
    template = file.read()

# Step 4: Replace placeholder with animal info
html_content = template.replace("__REPLACE_ANIMALS_INFO__", output)

# Step 5: Write the final animals.html file
with open("animals.html", "w") as file:
    file.write(html_content)

print("✅ animals.html generated! Open it in your browser.")
