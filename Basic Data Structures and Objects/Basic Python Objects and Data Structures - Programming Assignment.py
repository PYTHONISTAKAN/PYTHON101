"""Problem 1
Multiply the 3 numbers you get from the user and print them on the screen. Try to print to the screen using the *format* method.

Problem 2
Find the user's body mass index based on the height and weight values you get from the user.

Body Mass Index : Weight / Height(m) Height(m)

Problem 3
Take how much a vehicle burns per kilometer and how many kilometers it travels and calculate how much the driver has to pay in total.

Problem 4
Get the user's first name, last name and number and print them one after the other on the screen.

Problem 5
Ask the user for two numbers and exchange their values with each other.

Problem 6
Take two perpendicular sides (a,b) of a right triangle and try to find the length of the hypotenuse.

Hypotenuse Formula: a^2 + b^2 = c^2
"""

#Problem 1
a = int(input("1st number: "))
b = int(input("2nd number: "))
c = int(input("3rd number: "))

result = a * b * c

print("Multiplication of numbers = {}".format(result))

#Problem 2
height = float(input("Enter your height (m): "))
weight = float(input("Enter your weight (kg): "))

bmi = weight / (height ** 2)

print("Your Body Mass Index (BMI): {}".format(bmi))

#Problem 3

fuel_consumption = int(input("Enter your average fuel consumption per 100 km: "))  
fuel_price_per_liter = 10  
distance = int(input("Enter the distance you will travel (in km): "))  

fuel_needed = (distance * fuel_consumption) / 100  
total_cost = fuel_needed * fuel_price_per_liter  

print("The estimated travel cost is: {}".format(total_cost))

#Problem 4
name = input('name: ')
surname = input('surname: ')
telephone = int(input('Telephone number: '))
information = [name,surname,telephone]

print("name: {}\nSurname :{}\nPhonenumber: {}".format(information[0],information[1],information[2]))

#Problem 5
firstnumber= int(input("enter the first number: "))
secondnumber= int(input("enter the second number: "))
temp = firstnumber
firstnumber = secondnumber
secondnumber = temp
print("First number is {} and the second one is {}".format(firstnumber, secondnumber))

#Problem 6

#Formula: a^2 + b^2 = c^2

a = int(input("1st number: "))
b = int(input("2nd number: "))

c = (a**2 + b**2) ** 0.5
print("hypotenuse = {}".format(c))

