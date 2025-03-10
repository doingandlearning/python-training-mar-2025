print("Hello")

# first_name_of_user = input("What is your first name? ")   # snake case
first_name_of_user = "Kevin"
#                     01234    Cmd-/   Ctrl-/
print("Hello " + first_name_of_user)
print(type(first_name_of_user))
print(first_name_of_user.find("q"))

first_name_of_user = 73.37
print(first_name_of_user.is_integer())
print(first_name_of_user)
print(type(first_name_of_user))

first_name_of_user = True  # True False

print(first_name_of_user)
print(type(first_name_of_user))

# ' or " or """
new_string = """
I am a new string!


This is still part of the same string!
"""
print(new_string)
print(new_string.center(100))

print("Hello, " + str(first_name_of_user) + ", how are you today?")  # string concatention
print("Hello, {}, how are you today?".format(first_name_of_user))
print(f"Hello, {first_name_of_user}, how are you today?")
print(f"1 + 1 = {1 + 1}")

print("Hello world".replace("Hello", "Goodbye"))

new_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(new_string[3])   # what's at position 3
print(new_string[3:])  # from position 3 to the end
print(new_string[3:5])  # from position 3 up to but not including the character at position 5
print(new_string[::-1])
print(new_string[::2])

