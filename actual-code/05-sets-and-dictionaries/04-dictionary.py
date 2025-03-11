cities_dictionary = {
    "Italy": "Rome",
    "Spain": "Madrid",
    "France": "Paris",
    "Netherlands": {
        "captial": "Amsterdam",
        "airport": "S"
    }
}

# "key": "value"
#  - anything immutable can be a key!

print(cities_dictionary["Italy"])
print(cities_dictionary.get("Ireland", "Not on list"))  # get key and fallback!
print(cities_dictionary.keys())

for key in cities_dictionary.keys():
    print(f"The information we have about {key} is {cities_dictionary.get(key)}")

print(cities_dictionary.values())
print(cities_dictionary.items())



print("Italy" in cities_dictionary)  # checking whether the key exists!
print("Rome" in cities_dictionary)

user_dictionary = {
    "name": {
        "title": "Mr",
        "first_name": "Kevin",
        "last_name": "Cunningham"
    },
    "interests": ["3D Printing", "Local First Development", "Walking dog"]
}

print(f"{user_dictionary.get("name").get("first_name", "Someone")} likes {", ".join(user_dictionary.get("interests"))}")
print(f"{user_dictionary["name"]["first_name"]} likes {", ".join(user_dictionary.get("interests"))}")

cities_dictionary["Netherlands"] = "Amsterdam"
cities_dictionary["Ukraine"] = "Kiev"
print(cities_dictionary)

france = cities_dictionary.fromkeys(["France", "Italy"])
print(france)

