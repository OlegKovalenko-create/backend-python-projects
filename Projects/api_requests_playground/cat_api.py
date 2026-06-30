import requests

def cat_fact():
    try:
        r = requests.get("https://catfact.ninja/fact")
        data = r.json()
        return data["fact"]
    except:
        return "Ошибка получения факта"