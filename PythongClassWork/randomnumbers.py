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

import random

random_number = random.randint(1, 100)

guess = int(input("Enter a number between 1 and 100: "))

count = 0

while guess != random_number:
    if guess < random_number:
        count += 1
        print("Your guess is too low")
        guess = int(input("Enter a number between 1 and 100: "))
    elif guess > random_number:
        count += 1
        print("Your guess is too high")
        guess = int(input("Enter a number between 1 and 100: "))
    else:
        count += 1
        break

print("You are correct! The number is", random_number)
print("It took you", count, "times to get the right answer")





