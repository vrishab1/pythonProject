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

released = float(input("When was Python first released? "))

loop = True
while loop:
    if released != 1991:
        print("No, that's not it. Try again")
        released = float(input("When was Python first released? "))
    else:
        print("Congratulations! That is correct.")
        print("Bye!")
        loop = False
