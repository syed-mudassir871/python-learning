## create basic calculator
x = input("Enter first number: ")
y = input("Enter second number: ")

oper = input("Choose a math operation (+, -, *, /): ")


if oper == "+":
    print(int(x) + int(y))
elif oper == "-":
    print(int(x) - int(y))
elif oper == "*":
    print(int(x) * int(y))
elif oper == "/":
    print(int(x) / int(y))
