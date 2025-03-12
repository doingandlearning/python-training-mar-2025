"""
This is a very useful utility library.
- What can they expect to find here?
- Where have you used? What to look for? Documentation ...
"""


def printer(message):
    print("I'm about to print something.")
    print(message)
    print("Did I do okay?")


class Shape:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"This is shape of type {self.name}"


default_shape = Shape("circle")

def _private_function():
    print("I'm private - leave me alone!")

def main():
    print("My utils file has been loaded")
    print(f"The utils.py modules says its name is: {__name__}")


if __name__ == "__main__":
    main()