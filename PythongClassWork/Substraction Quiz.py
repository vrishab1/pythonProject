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


number1 = random.randint(1, 100)
number2 = random.randint(1, 100)

correctCount = 0
count = 0
numberofquestions = 5
while count < numberofquestions:


    if number1 < number2:
        number1, number2 = number1, number2

    answer = int(input("What is " + str(number1) + " - " + str(number2) + "? "))

    if number1 - number2 == answer:
        print("You are correct!")
        correctCount = correctCount + 1
    else:
        print("Your answer is wrong.\n", number1, "-",number2, "is", number1 - number2)

##Fix this one
