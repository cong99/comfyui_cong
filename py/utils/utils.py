import json


def load_json_file(file):
    with open(file, 'r') as file:
        data = json.load(file)
    return data
