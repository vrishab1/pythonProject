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
SALES_TAX = 0
number = int(input("Enter the number of items you would like: "))
cost = float(input("Enter the cost of item you would like: "))

price = cost * number
tax = price * SALES_TAX
total = price + tax

print("The total price is", total)