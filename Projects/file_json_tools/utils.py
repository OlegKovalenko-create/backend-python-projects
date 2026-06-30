import json

FILE = "data.json"

def load():
    try:
        f = open(FILE, "r")
        data = json.load(f)
        f.close()
        return data
    except:
        return []

def save(data):
    f = open(FILE, "w")
    json.dump(data, f)
    f.close()