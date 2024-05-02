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

for num in range (10,20):
    for i in range(2, num):
        if num % i == 0:
            j = num / i
            print(num, 'equals', i, "*", j)
            break
    else:
        print(num, "is a prime number")