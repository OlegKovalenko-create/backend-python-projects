import requests

def joke():
    try:
        r = requests.get("https://official-joke-api.appspot.com/random_joke")
        data = r.json()
        return data["setup"] + " - " + data["punchline"]
    except:
        return "Не получилось получить шутку"