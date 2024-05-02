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

inputstring = str(input("Enter a String: "))
secondstring = str(input("Enter a second string: "))

newstring1 = inputstring[:2] + secondstring[2:]
newstring2 = secondstring[:2] + inputstring[2:]

print(newstring1)
print(newstring2)

print(newstring1," ", newstring2)