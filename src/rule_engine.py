import json

def get_fix(root_cause):

    with open("rules/mappings.json", "r") as file:
        mappings = json.load(file)

    return mappings.get(root_cause)