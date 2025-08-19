'''Problem 1
Try to determine whether a number entered by the user is a perfect number.

A number is called a "perfect number" if the sum of its divisors (excluding itself) is equal to the number itself. For example, 6 is a perfect number. (1 + 2 + 3 = 6)'''

while True:
    y = input('Enter a number to check if it is a perfect number (Press "q" to exit): ')
    if y.lower() == 'q':  
        print("Exiting...")
        break
    if not y.isdigit():  
        print("Please enter a valid number!")
        continue
    x = int(y) 
    total = 0

    for i in range(1, x):
        if x % i == 0:
            total += i

    if total == x:
        print(f"{x} is a perfect number.")
    else:
        print(f"{x} is not a perfect number.")

'''Problem 2
Try to determine whether a number entered by the user is an "Armstrong" number.

For example, if a number has 4 digits and the sum of each digit raised to the power of 4 (for 3-digit numbers, raised to the power of 3) equals the number itself, then it is called an "Armstrong" number.

Example: 1634 = 1^4 + 6^4 + 3^4 + 4^4'''

while True:
    y = input("Welcome to the Armstrong number checker! Please enter a number ('Press q to exit'): ")
    if y.lower() == 'q':  
        print("Exiting...")
        break
    if not y.isdigit():  
        print("Please enter a valid number!")
        continue
    else:
        num_digits = len(y)
        total = sum(int(digit) ** num_digits for digit in str(y))
        if total == int(y):
            print("{} is an Armstrong number.".format(y))
        else:
            print("This is not an Armstrong number.")

'''Problem 3
Print the multiplication table for numbers from 1 to 10.

Hint: Use two nested for loops. Also, use the range() function to generate numbers.'''

for x in range(1, 11):    
    for y in range(1, 11):        
        result = x * y
        print("{} x {} = {}".format(x, y, result))

'''Problem 4
In each while loop iteration, take a number from the user and add it to a variable called "total." When the user presses "q," terminate the loop and print the "total" variable.

Hint: Start the while loop with an infinite condition and use break when the user presses "q".'''

print('Welcome to the infinite summation process')
total = 0
while True:    
    x = input("Please enter a number ('Press q to exit'): ")
    if x.lower() == 'q':
        print('Exiting...')
        break
    elif not x.isdigit():
        print("Please enter a valid number.")
    else:
        total += int(x)
        print(total)

'''Problem 5
Print only the numbers divisible by 3 from 1 to 100. Try to do this using continue.'''

print([x for x in range(1, 101) if x % 3 == 0])

for x in range(1, 101):
    if not x % 3 == 0:
        continue
    else:
        print(x, end=" ")

'''Problem 6
Using logical thinking and list comprehension, try to create a list containing only even numbers from 1 to 100.'''

print('')
print([x for x in range(1, 101) if x % 2 == 0])
