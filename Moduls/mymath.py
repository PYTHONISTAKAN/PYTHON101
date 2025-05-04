def addition(x, y):
    result = x + y
    return print(result)

def subtraction(x, y):
    result = x - y
    return print(result)

def multiplication(x, y):
    result = x * y
    return print(result)

def division(x, y):
    result = x / y
    return print(result)

def square_root(x):
    result = x ** 0.5
    return print(result)

def exponentiation(x):
    result = x ** 2
    return print(result)

def factorial(x):
    result = 1
    for i in range(1, x + 1):
        result *= i
    return print(result)

def gcd(x, y):  # GCD = Greatest Common Divisor (EBOB in English)
    result = 1
    for i in range(1, min(x, y) + 1):
        if x % i == 0 and y % i == 0:
            result = i
    return print(result)
    