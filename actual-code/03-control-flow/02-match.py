atomic_number = 6

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

match atomic_number:
    case 1:
        print("Hydrogen")
    case 2:
        print("Helium")
    case 3:
        print("Lithium")
    case 4:
        print("Beryllium")
    case 5:
        print("Boron")
    case _:
        print("Not handled yet")