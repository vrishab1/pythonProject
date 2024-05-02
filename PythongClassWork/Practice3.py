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

flavor = input("Enter flavor: [V]anilla or [C]arrot: "). lower()
people = int(input("How many people are you serving? "))
cost = 0.00

'''if flavor == "V":
    flavor = "Vanilla"
elif flavor == "C":
    flavor = "Carrot"

if flavor == "V" and people <= 14:
    cost = 8
elif flavor == "V" and 14 < people <= 20:
    cost = 18
elif flavor == "C" and people '''

if type == 'v':
    flavor = 'vanilla'
    if people <=14:
        cost = 8
        shape = 'round'
        print(f"You need a {shape} {flavor} case and costs ${cost:.2f}")
    elif people > 14 and people <= 20:
        cost = 18
        shape = "sheet cake"
        print(f"You need a {shape} {flavor} case and costs ${cost:.2f}")
    else:
        print("You will need more than one cake")

print("You need a round {flavor} t")

