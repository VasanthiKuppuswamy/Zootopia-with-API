import json

ANIMAL_FILE_PATH = "animals_data.json"
INPUT_HTML_FILE = "animals_template.html"
OUTPUT_HTML_FILE = "animals.html"
KEYWORD_PLACEHOLDER = "__REPLACE_ANIMALS_INFO__"


def load_data(file_path):
    """ Loads a JSON file """
    try:
        with open(file_path, "r", encoding="utf-8") as handle:
            return json.load(handle)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON content in '{file_path}'.")
        return


def get_animal_data():
    """ Returns the animal data from JSON file """
    return load_data(ANIMAL_FILE_PATH)


def get_filter(animals_data):
    """ Filter animal data by skin type."""
    skin_types = set([animal.get('characteristics', {}).get('skin_type') for animal in animals_data])
    # for handling missing data
    skin_types.add("Other")

    # Display available skin types to the user
    print("Available skin types:", ', '.join(skin_types))

    while True:
        # Ask user to select a skin type
        selected_skin_type = input("Enter a skin type from the list above: ")

        if selected_skin_type not in skin_types:
            print(f"Invalid choice. Please select a valid skin type from the list.")
            continue
        else:
            return selected_skin_type


def filter_and_generate_html(animals_data):
    """ Returns the animal data from JSON file """

    # get filtered skin type from user
    selected_skin_type = get_filter(animals_data)

    output = ['<ul class="cards">']

    for animal in animals_data:
        name = animal.get('name', 'Unknown')
        diet = animal.get('characteristics', {}).get('diet', 'Unknown')
        location = ' '.join(animal.get('locations', [])[0]) if 'locations' in animal else 'Unknown'
        animal_type = animal.get('characteristics', {}).get('type', 'Unknown')
        skin_type = animal.get('characteristics', {}).get('skin_type')

        # Skip animals that don't match the selected skin_type
        if selected_skin_type == "Other":
            if skin_type is not None:
                continue

        elif skin_type != selected_skin_type:
            continue

        output.append(f"""
        <li class="cards__item">
          <div class="card__title">{name}</div>
          <div class="card__text">
            <ul>
              <li><strong>Diet:</strong> {diet}</li>
              <li><strong>Location:</strong> {location}</li>
              <li><strong>Type:</strong> {animal_type}</li>
              <li><strong>Skin Type:</strong> {skin_type if skin_type else 'Unknown'}</li>
            </ul>
          </div>
        </li>
            """)

    output.append('</ul>')

    return '\n'.join(output)


def replace_keyword_in_html(input_file, keyword, replacement, output_file):
    """
    Reads an HTML file, replaces a keyword with a specified string,
    and optionally saves the modified content to a new file.
    """
    try:
        # Read the HTML file
        with open(input_file, "r", encoding="utf-8") as file:
            html_content = file.read()

        # Replace the keyword with the given string
        modified_html = html_content.replace(keyword, replacement)

        # Save to output file if specified
        if output_file:
            with open(output_file, "w", encoding="utf-8") as file:
                file.write(modified_html)
            print(f"Success: HTML file '{output_file}' has been created successfully.")

        return modified_html
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def main():
    # Get data
    animal_data = get_animal_data()

    formatted_animal_data = filter_and_generate_html(animal_data)

    # Get new html file
    replace_keyword_in_html(INPUT_HTML_FILE, KEYWORD_PLACEHOLDER, formatted_animal_data, OUTPUT_HTML_FILE)


if __name__ == '__main__':
    main()