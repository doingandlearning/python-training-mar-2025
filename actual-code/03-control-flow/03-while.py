
count = 10
while count >= 0:  # evaluate to True/False
    print(count)
    count -= 1

print("Blast off!")

command = ""

while command.lower() != "exit":
    command = input("You are in a dark room. What will you do?")
    match command.lower():
        case "look":
            print("You find a mysterious key.")
print("You have left the room.")

CORRECT_PASSWORD = "open_sesame"  # open says me
entered_password = None
number_of_tries = 0
access_granted = False

while entered_password != CORRECT_PASSWORD:
    if number_of_tries == 3:
        break

    entered_password = input("Enter the password")
    if entered_password == CORRECT_PASSWORD:
        access_granted = True
    number_of_tries += 1

if access_granted:
    print("Access granted")
else:
    print("Access denied")