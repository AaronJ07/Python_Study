#Operation in Python
# This module provides basic arithmetic operations

a = 10
b = 5

def add(a, b):
    """Returns the sum of a and b."""
    return a + b

def subtract(a, b):
    """Returns the difference of a and b."""
    return a - b

def multiply(a, b):
    """Returns the product of a and b."""
    return a * b

def divide(a, b):
    """Returns the quotient of a and b. Raises an error if b is zero."""
    if b == 0:
        print("Cannot divide by zero.")
    return a / b

def modulus(a, b):
    """Returns the remainder of a divided by b."""
    return a % b

def exponent(a, b):
    """Returns a raised to the power of b."""
    return a ** b

def floor_divide(a, b):
    """Returns the largest integer less than or equal to the division of a by b."""
    if b == 0:
        print("Cannot divide by zero.")
        return None
    return a // b

def absolute(a):
    """Returns the absolute value of a."""
    return abs(a)

def round_number(a, ndigits=0):
    """Returns a rounded version of a to ndigits decimal places."""
    return round(a, ndigits)

def increment(a, b=1):
    """Increments a by b. Default is 1."""
    return a + b

def decrement(a, b=1):
    """Decrements a by b. Default is 1."""
    return a - b

def negate(a):
    """Returns the negation of a."""
    return -a

def square(a):
    """Returns the square of a."""
    return a * a

print("Addition:", add(a, b))
print("Subtraction:", subtract(a, b))
print("Multiplication:", multiply(a, b))
print("Division:", divide(a, b))
print("Modulus:", modulus(a, b))
print("Exponentiation:", exponent(a, b))
print("Floor Division:", floor_divide(a, b))
print("Absolute Value:", absolute(-a))
print("Rounded Number:", round_number(3.14159, 2))
print("Increment:", increment(a))
print("Decrement:", decrement(a))
print("Negation:", negate(a))
print("Square:", square(a))