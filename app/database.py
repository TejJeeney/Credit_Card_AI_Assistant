import json

def load_cards():
    with open("app/cards.json") as f:
        return json.load(f)