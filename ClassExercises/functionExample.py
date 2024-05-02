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

companies = ["Apple","IBM", "X","Facebook"]
earnings = []
for i in range(len(companies)):
    num = random.randint(1,500000000)
    earnings.append(num)

print(f"The companies are {companies}")
print(f"Their earnings are {earnings}")

maxMoney = max(earnings)
indexMax = earnings.index(maxMoney)
indexCompany = companies[indexMax]
