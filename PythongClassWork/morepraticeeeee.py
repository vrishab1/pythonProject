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

first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
third = int(input("Enter third number: "))

if (first > second) & (first > third):
    print("The largest number is", first)
elif (second > first) & (second > third):
    print("The largest number is", second)
else:
    print("The largest number is", third)
