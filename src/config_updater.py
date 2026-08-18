import json

def update_config(config_file, changes):

    with open(config_file, "r") as file:
        config = json.load(file)

    for change in changes:

        parameter = change["parameter"]
        new_value = change["newValue"]

        config[parameter] = new_value

    with open(config_file, "w") as file:
        json.dump(config, file, indent=4)

    return config