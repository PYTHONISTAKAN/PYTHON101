"""Problem 1
Print all perfect numbers from 1 to 1000. To do this, write a function that returns whether a number is perfect or not.
A perfect number is a number whose sum of divisors equals itself. For example, 6 is a perfect number (1 + 2 + 3 = 6)."""

def perfect_number(x):
    if not isinstance(x, int):
        print("Please enter a valid number")
        return
    
    total = sum(y for y in range(1, x) if x % y == 0)  

    if total == x:
        print(f"{x} is a perfect number")
    else:
        print(f"{x} is not a perfect number")

perfect_number(6)
perfect_number(28)
perfect_number(12)

"""Problem 2
Write a function that takes 2 numbers from the user and returns their greatest common divisor (GCD)."""

def gcd(x, y):
    if not (isinstance(x, int) and isinstance(y, int)): 
        print("Please enter a valid number")
        return    

    while y:
        x, y = y, x % y  # Euclidean algorithm

    return x  

"""Problem 3  Do it for LCM"""
def lcm(x, y):
    if not (isinstance(x, int) and isinstance(y, int)): 
        print("Please enter a valid number")
        return    

    return abs(x * y) // gcd(x, y)  # LCM formula

# Test 
print(gcd(30, 60))  
print(gcd(48, 18))  

print(lcm(10, 20))  
print(lcm(12, 18))  

"""Problem 4
Take a two-digit number from the user and write a function that finds its pronunciation.

Example: 97 ---------> Ninety Seven"""

def read_number(x):
    if not isinstance(x, int):
        return "Please enter a valid number"
    
    if not (10 <= x < 100):  
        return "Please enter a number between 10 and 99."

    tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]

    tens_digit = x // 10  
    ones_digit = x % 10  

    pronunciation = tens[tens_digit]  
    if ones_digit != 0:  
        pronunciation += " " + ones[ones_digit]

    return pronunciation  

print(read_number(32))  
print(read_number(83))
print(read_number(80))  
print(read_number(99))  
print(read_number(5))   
print(read_number(105)) 
print(read_number("abc")) 

"""Problem 5
Write a function that prints Pythagorean triples for numbers from 1 to 100. (a <= 100, b <= 100)"""

def pythagorean():
    for x in range(1, 101):  
        for y in range(x, 101):  
            for z in range(y, 101):  
                if x**2 + y**2 == z**2:
                    print(f"Pythagorean Triple: {x}, {y}, {z}")

pythagorean()
