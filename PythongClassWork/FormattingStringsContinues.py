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
num = 1
meters = 39.67
kilometers = 1000 * meters

print(f"{"Inches":13s}{"Meters":25s}{"Kilometers":1s}")

for x in range (1,101):
    print(f"{x*num:>.2f}\t\t{x*meters:>.2f}\t\t{x*kilometers:>,.2f}")