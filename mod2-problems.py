# 1. Create a program that prints the following output to the screen: "Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony. Then, everything changed when the Fire Nation attacked."
print ("Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony. Then, everything changed when the Fire Nation attacked.")

# 2. Create a program that prompts for 2 numbers and then outputs the addition, subtraction, multiplication, and division of the first number by the second number.
#promting the user to input their numbers
print ("Lets do some math!")
firstnumber = input("Enter the first number: ")
secondnumber = input("Enter your 2nd number: ")
#math stuff
thesum = float(firstnumber) + float(secondnumber)
difference = float(firstnumber) - float(secondnumber)
product = float(firstnumber) * float(secondnumber)
division = float(firstnumber) / float(secondnumber)
#returnresults
print ("Sum:", thesum)
print ("Difference:", difference)
print ("Product:", product)
print ("Quotient:", division)

# 3. Create a program that prompts for the side lengths of a triangle and computes the area using Heron's formula. (https://en.wikipedia.org/wiki/Heron%27s_formula)
#importing the math module to do a square root function
import math
#prompt for input for the length of the sides of a triangle
print ("Let's find the area of a triangle!")
side1 = float(input("Enter the length of the first side of a triangle: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))
#creating variables for calculating the area using Heron's formula
semiperimeter = 0.5 * (side1 + side2 + side3)
radicand = float((semiperimeter-side1)*(semiperimeter-side3)*(semiperimeter-side2)*semiperimeter)
#printing the area of the triangle
print ("The area of your triangle is:", math.sqrt(radicand))

# 4. Create a program that computes different statistics given five numbers including the total, average, minimum, maximum, range, and standard deviation (https://en.wikipedia.org/wiki/Standard_deviation).
#importing the math module
import math
#importing the statistics module for calculating standard deviation
import statistics
#prompt the user for 5 numbers and store them as floats in a list
num1 = float(input("Enter Your first stat:"))
num2 = float(input("Enter Your second stat:"))
num3 = float(input("Enter Your third stat:"))
num4 = float(input("Enter Your fourth stat:"))
num5 = float(input("Enter Your fifth stat:"))
numberlist = [num1, num2, num3, num4, num5]
#calculate and print total
total = sum(numberlist)
print ("Total:",total)
#calculate and print average
average = (sum(numberlist)/len(numberlist))
print ("Average:", average)
#print the minimum and maximum
print ("Minimum:", min(numberlist))
print ("Maximum:", max(numberlist))
#print the range
print ("Range:", max(numberlist)-min(numberlist) )
#print the standard deviation
print ("Standard Deviation:", statistics.stdev(numberlist))
