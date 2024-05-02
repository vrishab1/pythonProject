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

number = random.randint(1, 100)
guess = int(input("enter a number between 1 and 100: "))
count = 1
while guess != number:
    if guess > number:
        count += 1
        print("Your guess is to high")
        guess = int(input("enter a number between 1 and 100: "))
    elif guess < number:
        count += 1
        print("Your guess is to low")
        guess = int(input("enter a number between 1 and 100: "))

print("You are correct! The number is", guess)
print("It took you", count, "times to get the right number!")