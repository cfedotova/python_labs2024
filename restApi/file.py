import json
import os

DATA_FILE = 'lab10.json'


class File:
    def __init__(self):
        if not os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'w') as f:
                json.dump([], f)

    def read_data(self):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)

    def write_data(self, data):
        with open(DATA_FILE, 'w') as f:
            json.dump(data, f, indent=2)
