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
# String repetition

string = input("Enter a word: ")
firstLetter = string[0]
newString = firstLetter + string[1:].replace(firstLetter,"#")
print(f"The new word is {newString}")