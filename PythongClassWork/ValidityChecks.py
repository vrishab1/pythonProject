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

positive = float(input("Enter a positive number greater than zero: "))

loop = True
while loop:
    if positive <= 0:
        print("The number must be positive--please try again")
        positive = float(input("Enter a positive number greater than zero: "))
    else:
        print("The number is", positive)
        loop = False





