import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def print_animal_info(animals: list):
    for animal in animals:
        name = animal.get("name", "")
        location = ", ".join(animal.get("locations", []))

        characteristics = animal.get("characteristics", {})
        diet = characteristics.get("diet", "")
        animal_type = characteristics.get("group", "")

        print(f"Name: {name}")
        print(f"Diet: {diet}")
        print(f"Location: {location}")

        if animal_type:
            print(f"Type: {animal_type}")
        print()


animals_data = load_data('animals_data.json')
print_animal_info(animals_data)
