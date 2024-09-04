from traceback import print_tb

numbers = [10, 20, 30, 40, 50]
x = 0
for number in numbers:
    print(number)
    x = x + number
    print(x)

print("================")

for k in range(1, 21):
    print(k)

print("================")
print("================")

## print even numbers
for k in range(0, 21, 2):
    print(k)
print("these are even numbers")

print("================")
print("================")

## print odd numbers
for k in range(1, 21, 2):
    print(k)
print("these are odd numbers")

print("================")
print("================")

## write table of 5
for t in range(1, 11):
    x = 5*t
    print("5  * ", t, " =", x)

print("================")
print("================")

## print right-angled triangle

# Set the number of rows for the triangle
rows = 5

# Outer loop for each row
for i in range(1, rows + 1):
    # Inner loop for printing stars in each row
    for j in range(i):
        print('*', end='')
    # Move to the next line after printing stars in a row
    print()

print("================")
print("================")

## print square

# Set the number of rows for square
x = 3

# Outer loop for each row
for i in range(x):
    # Inner loop for printing stars in each row
    for j in range(x):
        print('**', end='')
    print()
