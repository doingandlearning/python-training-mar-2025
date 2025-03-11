count = 10

player_dictionary = {}
test = ""
def add_new_player(name):
    global player_dictionary
    player_dictionary[name] = 1000
    global test
    test += "This is a test"

def some_other_function():
    # Why?
    player_dictionary["Someone else"] = 1000

add_new_player("Linh")
add_new_player("Fabian")
print(test)
some_other_function()
print(player_dictionary)


def increment_count(amount):
    # I have read access to any variable that is in the same file/scope/location
    global count  # use with care! With great power comes great responsibility
    count = count + amount


print(count)
increment_count(10)
print(count)
