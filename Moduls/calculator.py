import mymath

print(
    "Welcome to the Advanced Calculator!\n"
    "Please select the operation you want to perform:\n"
    "  Addition         : +\n"
    "  Subtraction      : -\n"
    "  Multiplication   : *\n"
    "  Division         : /\n"
    "  Square Root      : square_root\n"
    "  Exponentiation   : exponentiation\n"
    "  Factorial        : factorial\n"
    "  GCD (Greatest Common Divisor) : gcd\n"
    "  To EXIT, type: quit"
)

while True:
    x = input("Please enter an operation: ")
    
    if x == "+":
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        mymath.addition(a, b) 

    elif x == "-":
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        mymath.subtraction(a, b) 

    elif x == "*":
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        mymath.multiplication(a, b) 

    elif x == "/":
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        mymath.division(a, b) 

    elif x == "square_root":
        a = int(input("Enter the number: "))
        mymath.square_root(a)

    elif x == "exponentiation":
        a = int(input("Enter the number: "))
        mymath.exponentiation(a)

    elif x == "factorial":
        a = int(input("Enter the number: "))
        mymath.factorial(a)

    elif x == "gcd":
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        mymath.gcd(a, b)

    elif x == "quit":
        print("closing..")
        break

    else:
        print("Invalid operation, please try again.")