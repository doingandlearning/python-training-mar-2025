# file = open("logfile.txt", "a")  # w -> write, a -> append

# Pythonic way to interact with files ... handles closing automatically!
with open("logfile.txt", "a", newline="") as file:
    file.write("Gutentag\n")
    file.write("How are you?\n")
    file.write("Danke.\n")



with open("logfile.txt") as file:
    # next_line = file.readline()
    # while next_line:
    #     print(next_line)
    #     next_line = file.readline()
    for line in file.readlines():
        print(line.strip())  # .strip() removes newline characters and trailing or preceding whitespace
