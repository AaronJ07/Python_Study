#If-Else Statement

a = 10
b = 5
if a > b:
    print("a is greater than b")
else:
    print("a is less than b")

# If-Else Statement with Multiple Conditions
if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")
else:
    print("a is equal to b")

# Nested If-Else Statement
if a > 0:
    if b > 0:
        print("Both a and b are positive")
    else:
        print("a is positive, but b is not")

# If-Else with Logical Operators
if a > 0 and b > 0:
    print("Both a and b are positive")
elif a < 0 or b < 0:
    print("At least one of a or b is negative")