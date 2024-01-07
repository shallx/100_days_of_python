from art import logo

print(logo)

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1-n2

def divide(n1, n2):
    return n1/n2

def multiply(n1, n2):
    return n1*n2

operations = {
    "+": add,
    "-": sub,
    "/": divide,
    "*": multiply
}

num = int(input("What's the first number?: "))
for symbol in operations:
    print(symbol)


continued = True

while continued:
    operation_symbol = input("Pick an operation from the line above: ")
    num2 = int(input("What's the next number?: "))
    result = operations[operation_symbol](num,num2)

    print(f"{num} {operation_symbol} {num2} = {result}")
    num = result
    continued = input(f"Type 'y' to continue with {result}, or 'n' to exit: ") == "y"