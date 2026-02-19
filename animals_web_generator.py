import json
import re


def load_data(file_path):
    """ Loads a JSON file """

    with open(file_path, "r") as handle:
        return json.load(handle)


def load_html(file_path):
    """ Loads a HTML file """

    with open(file_path, "r") as file:
        return file.read()


def save_html(file_path, content):
    """ Saves a HTML file """

    with open(file_path, "w") as file:
        file.write(content)


def serialize_animal(location, name, diet, animal_type=""):
    """ Serialize an animal """
    
    output_string = ''

    output_string += '<li class="cards__item">'
    output_string += f'<div class="card__title">{name}</div><p class="card__text">\n'
    output_string += f"<strong>Diet: </strong>{diet}<br/>\n"
    output_string += f"<strong>Location: </strong>{location}<br/>\n"
    if animal_type:
        output_string += f"<strong>Diet: </strong>{animal_type}<br/>\n"
    output_string += '</p>\n</li>'

    return output_string


def animal_info(animals: list):
    """ Get info about animals """

    output = ''
    for animal in animals:
        location = ", ".join(animal.get("locations", []))
        name = re.sub(r'[^a-zA-Z0-9 ]', '', animal.get("name", "").strip())
        characteristics = animal.get("characteristics", {})
        diet = characteristics.get("diet", "").strip()
        animal_type = characteristics.get("group", "").strip()
        output += serialize_animal(location, name, diet, animal_type)

    return output


def main():
    animals_data = load_data('animals_data.json')
    animals_info = animal_info(animals_data)
    html_page = load_html("animals_template.html")
    html_with_animals = html_page.replace("__REPLACE_ANIMALS_INFO__", animals_info)
    save_html("animals.html", html_with_animals)


if __name__ == "__main__":
    main()
