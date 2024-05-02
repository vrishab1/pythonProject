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

'''
Question 3. Ask the user to enter a string with length 7,
keep asking the user to enter if the length is not 7,

Once the user enters correct input, show the middle 3 characters in Upper cases.
Sample output:
Please enter a string with 7 characters: python!
The final string is THO
'''

stringseven = str(input("Please enter a string with 7 characters: ")).upper()

newstringseven = stringseven[2:5]

while True:
    if len(stringseven) == 7:
        print("The final string is", newstringseven)
        break
    else:
        print("Please enter a string with 7 characters: ")



