import traceback


def divide_400_by_user_input():
    number_from_user = input("Give me a number: ")
    result = None
    try:
        number_from_user = int(number_from_user)
        result = 400 / number_from_user
        # open("non-existing-file")
    except ValueError:
        print("You passed something that can't be converted to a number. Try again.")
        divide_400_by_user_input()
    except ZeroDivisionError as exp:
        print("Whoops! You can't divide by zero! Try again.")
        divide_400_by_user_input()
    except Exception as exp:
        print("Something unexpected happened!")
        print(exp)
        error = traceback.format_exc()
        print(f"Captured traceback: {error}")
    else:  # will run only if everything was successful - no error was raised!
        print("This will run if no error was thrown!")
        print("Everything went well!")
    finally:  # clean up!
        print("This will run whether everything went well or not")

    return result

print(divide_400_by_user_input())
print("This still runs!")
