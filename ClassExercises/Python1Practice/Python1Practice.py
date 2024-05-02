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

TITLE_ONE = "Day"
TITLE_TWO = "price on day"
TITLE_THREE = "price increase"
ITEMA = 3.00/100
ITEMB = 5.20/100


price = float(input("Please enter the price of the item: "))
numberofdays = int(input("Enter number of days for which to print the price: "))
itemtype = input("Enter item type (A or B): ").upper()

if itemtype == "A":
    growth_rate = ITEMA
else:
    growth_rate = ITEMB


print(f"{TITLE_ONE} {TITLE_TWO} {TITLE_THREE}")

for day in range(numberofdays):
    print(day)
    #print(f"{i * day}/t/t{i * priceonday}/t/t{i * priceincrease}")



