"""
Class: CS230--Section 3
Name: Vrishab Bharti
Description: (Give a brief description for Exercise name--See
below)
I pledge that I have completed the programming assignment
independently.
I have not copied the code from a student or any source.
I have not given my code to any student. 
"""

first = float(input("enter the first number: "))
second = float(input("enter the second number: "))
third = float(input("enter the third number: "))

average = float(first + second + third)/3

print("The average of " + (str(first + second + third)) + " is " + str(round(average, 2)))