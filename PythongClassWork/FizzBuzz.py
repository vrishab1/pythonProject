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

for count in range (1,51):
    if count % 3 == 0 and count % 5 == 0:
        print("FizzBuzz")
    elif count % 5 == 0:
        print("Buzz")
    elif count % 3 == 0:
        print("Fizz")
    else:
        print(count)
