import os
import random
import yaml

def load_data():
    DATA_FILE = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data.yml")

    with open(DATA_FILE, "r") as fh:
        return yaml.safe_load(fh)

def random_option_for_key(data, key):
    return random.choice(data[key])

data = load_data()
selections = { key: random_option_for_key(data, key) for key in data.keys() }
selections.update({
    "name": "{first_name} {last_name}".format(**selections),
    "name_or_drink": random.choice(data["first_name"] + data["drink"]),
})

sentence = selections["sentence"]
print sentence.format(**selections)
