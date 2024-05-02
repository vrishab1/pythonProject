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
age = int(input("How old are you: "))

ticket = 0

if age < 3:
    print("Your ticket is free")
elif age >= 3 and age <= 12:
    ticket = 12
    print("Your ticket is $", ticket)
else:
    ticket = 15
    print("Your ticket is $", ticket)



