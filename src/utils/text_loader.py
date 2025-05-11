def load_text_descriptions(file_path):
    import json

    with open(file_path, 'r') as file:
        descriptions = json.load(file)

    return descriptions

def get_description_for_image(image_id, descriptions):
    return descriptions.get(image_id, "Description not found.")