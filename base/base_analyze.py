import yaml


def analyze_file(file_name):
    with open("./data/" + file_name + ".yml", 'r') as f:
        return yaml.load(f)

