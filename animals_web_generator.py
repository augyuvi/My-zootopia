import json
import html   # escape special characters


def load_data(file_path):
    """Loads a JSON file and returns its content"""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def clean_text(text):
    """
    Normalize weird characters:
    - Fix curly apostrophes and quotes
     have added this code because of an error for ( " Darwin's fox ")
    """
    if not isinstance(text, str):
        return text
    return (
        text.replace("â€™", "’")  # common broken apostrophe
            .replace("’", "'")
            .replace("“", '"')
            .replace("”", '"')
    )


def serialize_animal(animal):
    """Convert a single animal object into an HTML list item"""
    output = '<li class="cards__item">\n'

    # Title
    if "name" in animal:
        name = clean_text(animal["name"])
        output += f'  <div class="card__title">{html.escape(name)}</div>\n'

    # Body (fields as list items)
    output += '  <div class="card__text">\n'
    output += '    <ul class="card__details">\n'

    if "characteristics" in animal and "diet" in animal["characteristics"]:
        diet = clean_text(animal["characteristics"]["diet"])
        output += f'      <li class="card__detail"><strong>Diet:</strong> {html.escape(diet)}</li>\n'

    if "locations" in animal and len(animal["locations"]) > 0:
        location = clean_text(animal["locations"][0])
        output += f'      <li class="card__detail"><strong>Location:</strong> {html.escape(location)}</li>\n'

    if "characteristics" in animal and "type" in animal["characteristics"]:
        type_ = clean_text(animal["characteristics"]["type"])
        output += f'      <li class="card__detail"><strong>Type:</strong> {html.escape(type_)}</li>\n'

    if "characteristics" in animal and "lifespan" in animal["characteristics"]:
        lifespan = clean_text(animal["characteristics"]["lifespan"])
        output += f'      <li class="card__detail"><strong>Lifespan:</strong> {html.escape(lifespan)}</li>\n'

    if "characteristics" in animal and "color" in animal["characteristics"]:
        color = clean_text(animal["characteristics"]["color"])
        output += f'      <li class="card__detail"><strong>Color:</strong> {html.escape(color)}</li>\n'

    output += "    </ul>\n"
    output += "  </div>\n"
    output += "</li>\n"

    return output



# Step 1: Load data
animals_data = load_data("animals_data.json")

# Step 2: Generate HTML for all animals
output = ""
for animal in animals_data:
    output += serialize_animal(animal)

# Step 3: Read the HTML template
with open("animals_template.html", "r", encoding="utf-8") as file:
    template = file.read()

# Step 4: Replace placeholder with animal info
html_content = template.replace("__REPLACE_ANIMALS_INFO__", output)

# Step 5: Write the final animals.html file
with open("animals.html", "w", encoding="utf-8") as file:
    file.write(html_content)

print("✅ animals.html generated! Open it in your browser.")
