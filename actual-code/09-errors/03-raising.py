name = input("Give me your name: ")

if not name.istitle():
    raise Exception("Name must start with a capital letter.")
