"""Problem 1
Calculate the Body Mass Index (BMI) based on the height and weight values entered by the user, and display the following messages according to the rules:
BMI Formula: Weight / Height(m) * Height(m)
If BMI is below 18.5 -------> Underweight
If BMI is between 18.5 and 25 -------> Normal
If BMI is between 25 and 30 -------> Overweight
If BMI is above 30 -------> Obese
Problem 2
Get three numbers from the user and display the largest number.
Problem 3
Calculate the letter grade based on the midterm 1, midterm 2, and final exam grades entered by the user.
Midterm 1 will affect 30% of the total grade.
Midterm 2 will affect 30% of the total grade.
Final will affect 40% of the total grade.
Total Grade >= 90 -------> AA
Total Grade >= 85 -------> BA
Total Grade >= 80 -------> BB
Total Grade >= 75 -------> CB
Total Grade >= 70 -------> CC
Total Grade >= 65 -------> DC
Total Grade >= 60 -------> DD
Total Grade >= 55 -------> FD
Total Grade < 55 -------> FF
Problem 4
Now, let’s do a geometric shape calculation. First, ask the user whether they want to calculate the properties of a triangle or a quadrilateral.
If the user answers "Quadrilateral", ask for 4 sides and determine whether this quadrilateral is a square, rectangle, or an irregular quadrilateral.
If the user answers "Triangle", ask for 3 sides and determine whether this triangle is isosceles, equilateral, or an irregular triangle. If the given sides do not form a valid triangle, display the message "Not a triangle."""

# Problem 1 - BMI Calculation
print("Calculate the Body Mass Index (BMI)")
weight = float(input("Please enter your weight: "))
height = float(input("Please enter your height (m): "))
bmiformula = weight / (height * height)

if bmiformula < 18.5:
    print("Sorry to say that, but you are Underweight")
elif bmiformula >= 18.5 and bmiformula < 25:
    print("Your BMI is normal")
elif bmiformula >= 25 and bmiformula < 30:
    print("You are overweight")
else:
    print("Sorry to say that, but you are obese")
#Problem 2
print("Get three numbers from the user and display the largest number.")
a= int(input("please enter the first number"))
b= int(input("please enter the second number"))
c= int(input("please enter the third number"))
if a > b and a > c:
    print (a)
elif b> a and b>c:
    print (b)
else:
    print (c)
# Problem 3 - Letter Grade Calculation
print("Calculate the letter grade based on the midterm 1, midterm 2, and final exam.")
midterm1 = float(input("Please enter your midterm1 grade: "))
midterm2 = float(input("Please enter your midterm2 grade: "))
final = float(input("Please enter your final grade: "))
amidterm1 = (midterm1 * 30) / 100
amidterm2 = (midterm2 * 30) / 100
afinal = (final * 40) / 100
average = amidterm1 + amidterm2 + afinal

if average >= 90:
    print("Average is AA")
elif average >= 85:
    print("Average is BA")
elif average >= 80:
    print("Average is BB")
elif average >= 75:
    print("Average is CB")
elif average >= 70:
    print("Average is CC")
elif average >= 65:
    print("Average is DC")
elif average >= 60:
    print("Average is DD")
elif average >= 55:
    print("Average is FD")
else:
    print("Average is FF")
#Problem 4
print("triangle or quadrilateral?")
gscalculation= input("which do you want to calculate please enter 'triangle' or 'quadrilateral'")
if gscalculation == "triangle":
    print("please enter 3 sides of triangle")
    a= int(input("first side of triangle"))
    b= int(input("second side of triangle"))
    c= int(input("third side of triangle"))

    if a + b > c and a + c >b and b + c > a:
        if a == b and a == c:
            print("this is a equilateral triangle")
        elif (a == b and a!= c ) or (a == c and a !=b):
            print("this is a isosceles triangle")
        else:
            print("this is a  irregular triangle")
    else: 
        print ("this is not a triangle")

elif gscalculation == "quadrilateral":
    print("please enter 4 sides of quadrilateral")
    x= int(input("first side of quadrilateral"))
    y= int(input("second side of quadrilateral"))
    z= int(input("third side of quadrilateral"))
    q= int(input("fourth side of quadrilateral"))

    if x+y+z>q and x+y+q>z and x+z+q>y and y+z+q>x:
        if(x == y== z == q):
            print("this is a square")
        elif (x==y or x== z or x == q) or (y==x or y==z or y==q) or (z==x or z==y or z==q):
            print("this is a Rectangle ")
        else:
            print("this is a quadrilateral")
    else:
        print("this is not valid quadrilateral")