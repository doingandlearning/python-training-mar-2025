# iterator -> lists, tuples, strings, ...
for number in range(10):
    if number % 2 == 0:  # some test for elements we want to skip
        print("We don't like even numbers!")
        break
    # some kind of processing going on here!!
    print(number)
else:
    print("All numbers were processed.")
# for character in "Hello":
#     print(character)

number = int(input("Give me a number: "))
print(number == 12)  #
print(type(number))