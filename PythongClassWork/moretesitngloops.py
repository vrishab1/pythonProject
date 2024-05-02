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
for count in range (0, 31, 3):
    print(count, end=" ")
    print()

for count in range (31, 0, -1):
    print(count, end=" ")
print()

for count in range(25, 0, -2):
    print(count, end=" ")
print()

lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))
theSum = 0

for number in range (lower, upper + 1):
    theSum = theSum + number
    print(theSum)