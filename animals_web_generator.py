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


def add_if_exists(title, characteristic):
    if characteristic:
        return f"<li><strong>{title}: </strong>{characteristic}</li>\n"
    return ""


def serialize_animal(all_animal_info):
    """ Serialize an animal """

    output_string = ''
    location, name, diet, temperament, color, lifespan, animal_type = all_animal_info

    output_string += '<li class="cards__item">'
    output_string += f'<div class="card__title">{name}</div><br>\n'
    output_string += f'<div class="card__text">\n'
    output_string += "<ul>\n"
    output_string += add_if_exists("Diet", diet)
    output_string += add_if_exists("Location", location)
    output_string += add_if_exists("Temperament", temperament)
    output_string += add_if_exists("Color", color)
    output_string += add_if_exists("Lifespan", lifespan)
    output_string += add_if_exists("Group", animal_type)
    output_string += "</ul>\n"
    output_string += '</div>\n'
    output_string += "</li>"

    return output_string


def animal_info(animals: list):
    """ Get info about animals """

    output = ''
    for animal in animals:
        location = ", ".join(animal.get("locations", []))
        name = re.sub(r'[^a-zA-Z0-9 ]', '', animal.get("name", "").strip())
        characteristics = animal.get("characteristics", {})
        diet = characteristics.get("diet", "").strip()
        temperament = characteristics.get("temperament", "").strip()
        color = characteristics.get("color", "").strip()
        lifespan = characteristics.get("lifespan", "").strip().replace("â€“", " - ")
        animal_type = characteristics.get("group", "").strip()

        all_animal_info = location, name, diet, temperament, color, lifespan, animal_type

        output += serialize_animal(all_animal_info)

    return output


def main():
    animals_data = load_data('animals_data.json')
    animals_info = animal_info(animals_data)
    html_page = load_html("animals_template.html")
    html_with_animals = html_page.replace("__REPLACE_ANIMALS_INFO__", animals_info)
    save_html("animals.html", html_with_animals)


if __name__ == "__main__":
    main()
