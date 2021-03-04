import json


def read_json_from_file(filename):
    with open(filename, "r") as file:
        content = json.loads(file.read())
    return content


def write_json_to_file(content, filename):
    with open(filename, "w") as file:
        file.write(json.dumps(content))
