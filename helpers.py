import json
import os

def load_data():
    base_dir = os.path.dirname(os.path.dirname(__file__))  
    file_path = os.path.join(base_dir, "data", "test_data.json")

    with open(file_path, "r") as f:
        return json.load(f)