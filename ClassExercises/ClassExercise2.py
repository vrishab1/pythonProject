"""
Class: CS230--Section 3
Name: Vrishab Bharti
Description:
Exercise 1: Print the first ten odd numbers. Then, Print the first five multiples of 10.
Exercise 2: Write a program to ask the user for a number and calculate the sum of all numbers from 1 to that number:
Exercise 3: Write a program that asks the user to enter positive numbers and count how many are multiples of four or multiples of eight. When they enter 0, the program stops and prints a summary.
Exercise 4: Use a loop to print the following sequence:
Exercise 5: Find the total of the numbers from 1 to 100 but only add those numbers that are multiples of three or five.
Exercise 6: Ask the user for a number to create a series. Also ask the user for how many numbers should appear in the series. Display the series and its total.

I pledge that I have completed the programming assignment
independently.
I have not copied the code from a student or any source.
I have not given my code to any student. 
"""

print('Exercise 1: Print the first ten odd numbers & Print the first five multiples of 10')
#Exercise #1 uses range and Modulo
print("The first 10 odd numbers are:")
for num in range (20):
    if num % 2 == 0:
        continue
    print(num)

print()

print("The first five multiples of 10 are: ")
for num2 in range (1, 51):
    if num2 % 10 != 0:
        continue
    print(num2)

print('\nExercise 2: Number and calculate sum of all numbers from 1 to Number')
#Exercise #2: Sum and for loop
usernumber = int(input("Enter a number: "))

theSum = 0
for i in range(1, usernumber + 1):
    theSum += i
print("The total is:", theSum)

print('\nExercise 3: Enter Positive Numbers and count how many are multiples of four or multiples of eight. If 0 entered, program stops and prints summary')
#Exercise #3: For and if elif and else loops


multiples4 = 0
multiples8 = 0

while True:
    positivenumber = int(input("Enter a positive number: "))
    if positivenumber == 0:
        break
    if positivenumber % 4 == 0:
        multiples4 += 1
    if positivenumber % 8 == 0:
        multiples8 += 1
print("You entered",multiples4,"multiples of 4 and",multiples8, "multiples of 8.")

print('\nExercise 4: Use a loop to print')
#Exercise #4: For loops

num = 0
for i in range(12, 90, +11):
    i += num
    print(i, end=", ")

print('\n\nExercise 5: Find the total of the numbers from 1 to 100 but only add those numbers that are multiples of three or five.')
#Exercise #5: if elif function loops and Modulo

total = 0

for i in range (1, 101):
    if i % 3 == 0:
        total += i
    elif i % 5 == 0:
        total += i

print("The total of the numbers from 1 to 100 that are multiples of three or five is", str(total) + ".")

print('\n\nExercise 6: Ask the user for a number to create a series. Also ask the user for how many numbers should appear in the series. Display the series and its total.')
#Exercise #6: Using string and integers and for loops

starting = int(input("Enter a starting number: "))
terms = int(input("Enter number of terms: "))
sumofseries = 0

for i in range(terms):
    series = int(str(starting) * (i + 1))
    print(series, end=', ')
    sumofseries += series

print("\nThe sum of the series is:", sumofseries)
