def add(a, b):
    if not isinstance(a, (int, float)):
        raise TypeError("Parameter must be a number (float or int).")

    if not isinstance(b, (int, float)):
        raise TypeError("Parameter must be a number (float or int).")

    return a + b


def subtract(a, b):
    return a - b
