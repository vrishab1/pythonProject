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
number = float(input("Please enter a number between 1 and 10, inclusion: "))

loop = True
while loop:
    if number < 1 or number > 10:
        print('Invalid number.')
        number = float(input("Please enter a number between 1 and 10, inclusion: "))
    else:
        loop = False

print("The number you entered is", number)
