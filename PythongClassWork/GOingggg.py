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

menuchoice = True

while menuchoice:
    choice = int(input("""
    1 - Option 1,
    2 - Option 2,
    3 - Option 3,
    4, Quit
    Enter choice: """))
    if choice == 1:
        print("You chose option 1.")
    elif choice == 2:
        print("You chose option 2.")
    elif choice == 3:
        print("You chose option 3.")
    else:
        menuchoice = False

print("You have quit the menu")