"""
Class: CS230--Section 3
Name: Vrishab Bharti
Description:
Exercise 1: Print the sum of the numbers in a list, except ignore sections of numbers between a 6 and a 7 (every 6 will be followed by at least one 7). Print a message if there are no elements in the list.
Exercise 2: Create a list of ten (10) random integers from 1 to 100. Computer the difference between the largest and the smallest number in the list.
Exercise 3: Create two lists of numbers that have the same number of elements (please do not ask the user for the elements in the lists). Create a for loop that iterates through the two lists and calculates the difference between the respective elements of each list. Also. in the for loop, find the difference squared and keep a running total of that number.
Print the difference after each time it is calculated and the sum at the end of program. The output might look like this (use f-string formatting for the output)
Exercise 4: Create a list that has one or two numbers in it that are duplicated. Display the list and ask the user to remove one of the numbers. Use a function to remove duplicate numbers.
Exercise 5: Write a program to add item 7000 after 6000 in the following Python List.
Exercise 6: Write a program that reads in a series of scores and then assigns grades based on the following scheme--please note that this does NOT use the "standard" method of scores:

I pledge that I have completed the programming assignment
independently.
I have not copied the code from a student or any source.
I have not given my code to any student.
"""

print("\nExercise 1: Print the sum of the numbers in a list, except ignore sections of numbers between a 6 and a 7 (every 6 will be followed by at least one 7). Print a message if there are no elements in the list.")
##Using lists, boolean, for loops and if else loops
lists = [[24, 5, 1, 6, 7, 54, 6], [8, 6, 9, 7, 5, 32, 55, 79, 88]]

for i in lists:
    overall = 0
    ignore = False
    for num in i:
        if num == 6:
            ignore = True
        elif num == 7 and ignore:
            ignore = False
        elif not ignore:
            overall += num
    print(f"\nThe original list is {i}")
    if i:
        print(f"The total is {overall}")
    else:
        print("There are no elements in the list.")

print("\nExercise 2: Create a list of ten (10) random integers from 1 to 100. Computer the difference between the largest and the smallest number in the list.")
##Using Random, max and min

import random

lists = [random.randint(1, 100) for i in range(10)]
maxlist = max(lists)
minlist = min(lists)
difference = maxlist - minlist

print(f"\nThe difference between {maxlist} and {minlist} is {difference}")

print("\nExercise 3: Create two lists of numbers that have the same number of elements (please do not ask the user for the elements in the lists). Create a for loop that iterates through the two lists and calculates the difference between the respective elements of each list. Also. in the for loop, find the difference squared and keep a running total of that number.Print the difference after each time it is calculated and the sum at the end of program.")
##Using lists and for loops and decimals and exponential operators

list1 = [0.9, 1.7, 9.9, 3.5, 6.9, 9.0]
list2 = [4.5, 9.9, 0.3, 0.2, 5.8, 3.6]

print(f"\nThe first list is {list1}")
print(f"The second list is {list2}\n")

total_difference_squared = 0

for i in range(len(list1)):
    difference = list1[i] - list2[i]
    print(f"Difference is: {difference:.3f}")
    total_difference_squared += difference ** 2

print(f"\nThe sum of the differences squared is: {total_difference_squared:.3f}")

print("\nExercise 4: Create a list that has one or two numbers in it that are duplicated. Display the list and ask the user to remove one of the numbers. Use a function to remove duplicate numbers.")
##Using Lists, input, remove

lista = [9, 100, 45, 45, 100, 45, 15, 100, 250, 100]
print(f"\nThe list is {lista}")
duplicatedremoved = int(input("Enter a number that is duplicated to be removed from the list: "))

while duplicatedremoved in lista:
    lista.remove(duplicatedremoved)

print(f"The updated list is {lista}")

print("\nExercise 5: Write a program to add item 7000 after 6000 in the following Python List.")
##This one drills into the 3rd list as it inserts into it.

list1 = [[10, 20, [300, 400, [5000, 6000], 500], 30, 40]]
print(f"The original list is {list1}")
list1[0][2][2].insert(2, 7000)
print(f"The updates list is {list1}")

print("\nExercise 6: Write a program that reads in a series of scores and then assigns grades based on the following scheme--please note that this does NOT use the 'standard' method of scores: The grade is A if the score is >= best - 10 The grade is B if the score is >= best - 20 The grade is C if the score is >= best - 30 The grade is D if the score is >= best - 40")
##This one uses strip and split as well as max and if elif loops

seriesofgrades = input("\nEnter a series of grades, separated by commas: ")
seriesofgrades = [int(score.strip()) for score in seriesofgrades.split(',')]
print(f"The list is {seriesofgrades}")

bestscore = max(seriesofgrades)

grades = []

for i in seriesofgrades:
    if i >= bestscore - 10:
        grades.append('A')
    elif i >= bestscore - 20:
        grades.append('B')
    elif i >= bestscore - 30:
        grades.append('C')
    elif i >= bestscore - 40:
        grades.append('D')

for i in range(len(grades)):
    print(f"The grade of student{i} is {grades[i]}")


