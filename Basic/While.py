#While Loop

i = 1
while i <= 5:
    print(f"Current value of i: {i}")
    i += 1

# While Loop with Break
i = 1
while i <= 7:
    if i == 6:
        print("Breaking the loop at i = 6")
        break
    print(f"Current value of i: {i}")
    i += 1

# While Loop with Continue
i = 0
while i < 10:
    i += 1
    if i == 5:
        print("Skipping the iteration when i = 5")
        continue
    print(f"Current value of i: {i}")

# While Loop with Else
i = 1
while i <= 5:
    print(f"Current value of i: {i}")
    i += 1
else:
    print("Loop completed successfully, i is now greater than 5")

# Infinite While Loop (Use with caution)
i = 1
while True:
    print(f"Current value of i: {i}")
    i += 1
    if i > 5:
        print("Breaking the infinite loop at i = 6")
        break

# While Loop with Counter
counter = 0
while counter < 5:
    print(f"Counter is at: {counter}")
    counter += 1

# While Loop with Condition Check
number = 10
while number > 0:
    print(f"Current number: {number}")
    number -= 2

# While Loop with List Iteration
items = ['apple', 'banana', 'cherry']
index = 0
while index < len(items):
    print(f"Item at index {index}: {items[index]}")
    index += 1