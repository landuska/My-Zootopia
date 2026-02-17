import json


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


def animal_info(animals: list):
    """ Get info about animals """
    output = ''
    for animal in animals:
        location = ", ".join(animal.get("locations", []))
        name = animal.get("name")
        characteristics = animal.get("characteristics", {})
        diet = characteristics.get("diet", "")
        animal_type = characteristics.get("group", "")

        output += '<li class="cards__item">'
        output += f"Name: {name}<br/>\n"
        output += f"Diet: {diet}<br/>\n"
        output += f"Location: {location}<br/>\n"
        if animal_type:
            output += f"Diet: {animal_type}<br/>\n"
        output += '</li>'

    return output


def main():
    animals_data = load_data('animals_data.json')
    animals_info = animal_info(animals_data)
    html_page = load_html("animals_template.html")
    html_with_animals = html_page.replace("__REPLACE_ANIMALS_INFO__", animals_info)
    save_html("animals.html", html_with_animals)


if __name__ == "__main__":
    main()
