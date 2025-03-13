import csv

with open("test.csv", "w") as file:
    # writer = csv.writer(file)  # writer -> expecting ordered lists for each row
    writer = csv.DictWriter(file, fieldnames=["english_title", "release_year", "italian_title"])  # DictWriter
    writer.writeheader()
    writer.writerow({"english_title": "Men in Black II", "release_year": 2002, "italian_title": "Men in Black II"})
    writer.writerow({
        "english_title": "The Emperor's New Groove",
        "release_year": 2000,
        "italian_title": "Le follie dell'imperatore"
    })
    writer.writerow({"italian_title": "La sposa cadavere", "english_title": "Corpse Bride"})




