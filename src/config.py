import json
from pathlib import Path


def load_config():
    config_file = Path("config.json")

    with open(config_file, "r") as file:
        config = json.load(file)

    return config
