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
number = int(input("Enter the number of items you would like: "))
cost = float(input("Enter the cost of item you would like: "))

price = cost * number
tax = price * .05
total = price + tax

print("The total price is", total)
print("The total price is", round(total, 2))
print("The total price is $", round(total, 2))
print("The total price is $"+ str(round(total, 2)))