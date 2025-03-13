file = open("logfile.txt", "a")  # w -> write, a -> append

# writing to a file destroys the original if it exists and creates a new one.

file.write("Gutentag\n")
file.write("How are you?\n")
file.write("Danke.\n")

file.close()
