import requests
import json


def get_data(url, id):
    try:
        response = requests.get(url)
        response.raise_for_status()
        response = response.json()
        with open(f"{id}.txt", "w") as file:
            file.write(json.dumps(response))
    except Exception as e:
        print(e)

# threading!
for i in range(1, 11):
    get_data(f"https://swapi.dev/api/people/{i}", i)