import csv

# with open("test.csv") as file:
#     reader = csv.reader(file)  # iterator
#     headers = next(reader)
#     print(f"This is the header row: {headers}")
#     for row in reader:
#         if not row[1]:
#             row[1] = "an unknown year"
#         print(f"The movie {row[0]} was released in {row[1]} and in Italy was released as {row[2]}")


# \n\r
with open("test.csv") as file:
    reader = csv.DictReader(file)  # iterator
    for row in reader:
        if not row["release_year"]:
            row["release_year"] = "an unknown year"
        print(f"The movie {row["english_title"]} was released in {row["release_year"]} and in Italy was released as {row["italian_title"]}")