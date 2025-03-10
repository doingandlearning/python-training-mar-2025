num1 = 10

if num1 > 10:  # Evaluate to True or False!
    print("Number greater than 10!")


if num1 is None:
    print("It is a None")

if "ALLUPPER".isupper():
    print("Yup all uppercase! Stop shouting!")

if num1.is_integer():
    print("It is an int")

if num1 % 2 == 0:
    print("Number is even!")

print("Do some more work down here.")

if num1 > 10:
    print("It's bigger than 10")
else:
    print("It's less than 10 or equal to 10")

atomic_number = 4

if atomic_number == 1:
    print("Hydrogen")
elif atomic_number == 2:  # contracts else if -> elif
    print("Helium")
elif atomic_number == 3:
    print("Lithium")
else:
    print("Not handled yet!")

atomic_number = 5
if atomic_number <= 5:
    if atomic_number == 1:
        print("Hydrogen")
    elif atomic_number == 2:  # contracts else if -> elif
        print("Helium")
    elif atomic_number == 3:
        print("Lithium")
    elif atomic_number == 4:
        print("Beryllium")
    elif atomic_number == 5:
        print("Boron")
    else:
        print("Really not handled yet!")

# cyclomatic complexity


# ternary operator
# test ? result_when_true : result_when_false
age = 20
is_teenager = True if age > 12 and age < 20 else False  # short if expression
print(is_teenager)

is_teenager = None
if 12 < age < 20:
    is_teenager = True
else:
    is_teenager = False

print(is_teenager)


if "":
    print("None zero string")