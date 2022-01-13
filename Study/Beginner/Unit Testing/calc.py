def add(x, y):
    """Returns a sum of two parameters"""
    return x + y


def subtract(x, y):
    """Return a result of subtraction"""
    return x - y


def multiply(x, y):
    """Returns result of multiplication of two parameters"""
    return x * y


def divide(x, y):
    """Returns a result of division, raises an exception
        if there is an attempt to divide by zero"""
    if y == 0:
        raise ZeroDivisionError
    return x / y
