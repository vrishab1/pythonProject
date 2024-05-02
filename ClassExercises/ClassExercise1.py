"""
Class: CS230--Section 3
Name: Vrishab Bharti
Description:
Exercise 1: Write a program that asks the user for the Celsius temperature and converts it to Fahrenheit and Kelvin.
Exercise 2: Write a program that takes as inputs the hourly wage and overtime hours, and displays an employee's total weekly pay like this (round to two decimal places)
Exercise 3: You ask the user for a four-digit number and then add the total of the digits, such that the prompt and the output would look like the following (example on document)
Exercise 4: Have the user enter the number of people at the party that will be eating pizza and output the number of slices each one gets.  As you know the pizza might not be divided evenly. There are two ways to handle this. The first is to ignore the extra pieces and give everyone the same amount. The second way is to cut up the extra pieces so that everyone gets the same amount.
Exercise 5: Ask the user for an integer (n) and determine the total of n + nn + nnn. This means that if n=5, then nn is 55, and nnn is 555.


I pledge that I have completed the programming assignment
independently.
I have not copied the code from a student or any source.
I have not given my code to any student. 
"""

print('Exercise 1: Program for Celsius and Fahrenheit')
#Exercise #1 is simply math based
celsius = float(input('Enter Celsius temperature: '))

fahrenheit = (1.8*celsius)+32
kelvin = celsius + 273.15

print('The Celsius temperature of ', int(celsius),  ' is ', fahrenheit, ' degrees Fahrenheit')
print('The Kelvin temperature of ', int(celsius), ' is ', kelvin, ' degrees Kelvin')

print('\nExercise 2: Employees weekly pay using hourly wage and overtime pay')
#Exercise 2 looks into rounding to two decimal places and more math
hourlywage = float(input('Enter the hourly wage: '))
overtimeworked = float(input('Enter the overtime pay: '))

hourlypay = hourlywage * 40
overtimepay = overtimeworked * 1.5 * hourlywage

weeklypay = hourlypay + overtimepay

print("The employee's weekly pay is $", round(weeklypay, 2))

print('\nExercise 3: Adding four-digit number')
#Exercise 3 uses Modules, specifically using Modulo and integer division
number = int(input('Enter a four-digit number: '))
first = number // 1000
second = (number % 1000) // 100
third = (number % 100) // 10
fourth = number % 10

print("The sum of the digits in " + str(number) + " is " + str(first + second + third + fourth) + ".")

print('\nExercise 4: Program for Pizza with both options')
#Exercise 4 uses Modulo, integer division, and integers with two options
guests = float(input("Number of Guests: "))

sameamount = 32 // guests
leftover = 32 % guests

extraslices = 32 / guests

print("Option 1:", int(sameamount), "slices each,", int(leftover), "left over")

print("Option 2:", str(extraslices), "slices each")

print('\nExercise 5: Program for Integer(n) and total result')
#Exercise 5 is adding using integers that dont change character, add them, and then changing them at the end

n = int(input("Enter a number: "))
integern1 = n
integern2 = str(n) + str(n)
integern3 = str(n) + str(n) + str(n)

resultinteger = integern1 + int(integern2) + int(integern3)

print("The result is: ", resultinteger)
