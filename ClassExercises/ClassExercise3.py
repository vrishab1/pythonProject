"""
Class: CS230--Section 3
Name: Vrishab Bharti
Description:
Exercise 1: A program that asks the user for a single word and prints the word backwards, printing each letter on the same line, except backwards.
Exercise 2: A program that asks the user for a string and counts the number of letters, digits, and special symbols in a string.
Exercise 3: A program that prints the following, using as the string "Programming in Python"
Exercise 4: A program to create a new string made of the middle three characters of an input string.
Exercise 5: A program that takes a string and shifts it to the right and to left a given number of characters. Check that the number of characters to be shifted is less than the length of the string.
Exercise 6: A program that asks the user for two strings. The first string needs to be at least two characters long and the second string needs to be at least three characters long.
Exercise 7: A program that creates a string with a name and prints the output exactly as below (you can use your own name). Use f-strings in formatting your output and do not "hard code" your program.
I pledge that I have completed the programming assignment
independently.
I have not copied the code from a student or any source.
I have not given my code to any student. 
"""

print('Exercise 1: Write a program that asks the user for a single word and prints the word backwards, printing each letter on the same line, except backwards, such that the prompt and the output look like the following')
#Exercise #1 uses slice the string backwords and format strings

word = input("Enter a string: ")
newword = word[::-1]
print(f"The string, {word}, backwords, is {newword}")

print('\nExercise 2: A program that asks the user for a string and counts the number of letters, digits, and special symbols in a string.')
#Exercise #2 uses char, isdigit, isalpha and format strings

sampleword = input("Enter a sample string: ")
print(f"The total count of chars, digits, and symbols in {sampleword}")

CHARACTERSCOUNT = 0
DIGITSCOUNT = 0
SYMBOLSCOUNT = 0

for char in sampleword:
    if char.isdigit():
        DIGITSCOUNT += 1
    elif char.isalpha():
        CHARACTERSCOUNT += 1
    else:
        SYMBOLSCOUNT += 1


print(f"Characters = {CHARACTERSCOUNT}, Digits = {DIGITSCOUNT}, Symbol = {SYMBOLSCOUNT}")

print('\nExercise 3: Write a program that prints the following, using as the string "Programming in Python"')
#Exercise #3 uses len, find, count, ranges, upper, lover, replace

samplestring = "Programming in Python"
print("#1 Print the length of the string:",len(samplestring))
print("#2 Print the position where 'in' appears the first time is:",samplestring.find("in"))
print("#3 Print the number of times 'n' appears is:",samplestring.count("n"))
print("#4 Print the number of spaces is:",samplestring.count(" "))
print("#5 Print the substring 'Pro':",samplestring[0:3])
print("#6 Print the substring 'thon':",samplestring[17:21])
print("#7 Print the substring 'Programming in Py':", samplestring[0:17])
print("#8 Split the string at the spaces:",samplestring.split())
print("#9 Print the substring 'a':", samplestring[5])
print("#10 Print the string in uppercase:", samplestring.upper())
print("#11 Print the string in lowercase:", samplestring.lower())
print("#12 Print the string but replace 'in' with 'with':", samplestring.replace(" in ", " with "))


print("\nExercise 4: Write a program to create a new string made of the middle three characters of an input string.")
#Exercise #4 uses len, integer division, slicing with math/shifts, f - format

originalstring = input("Enter a string: ")
dividedmiddle = len(originalstring) // 2
middlecharacter = originalstring[dividedmiddle - 1:dividedmiddle + 2]
print("The middle three characters are:", middlecharacter)


print("\nExercise 5: A program that takes a string and shifts it to the right and to left a given number of characters. Check that the number of characters to be shifted is less than the length of the string.")
#Exercise #5 uses len, ranges, f - format, slicing with math and negatives

Stringinput = input("Enter a string: ")

while True:
    RotatedCharacters = int(input("Enter number of characters to rotate--the number must be less than the number of characters in the string: "))
    if RotatedCharacters < len(Stringinput):
        break
    else:
        continue

rotatedleft = Stringinput[RotatedCharacters:] + Stringinput[:RotatedCharacters]
rotatedright = Stringinput[-RotatedCharacters:] + Stringinput[:-RotatedCharacters]

print(f"The string, {Stringinput}, rotated to the left {RotatedCharacters} characters is {rotatedleft}")
print(f"The string, {Stringinput}, rotated to the right {RotatedCharacters} characters is {rotatedright}")


print("\nExercise 6: A program that asks the user for two strings. The first string needs to be at least two characters long and the second string needs to be at least three characters long.")
# Exercise 6 Uses addition, length, while

firststring = input("Enter first string: ")
while len(firststring) < 2:
    firststring = input("String must be at least two characters long! Please re-enter: ")

secondstring = input("Enter second string: ")
while len(secondstring) < 3:
    secondstring = input("String must be at least three characters long! Please re-enter: ")

newstring = firststring + secondstring + secondstring + firststring

print("The new string is", newstring)


print("\nExercise 7: A program that creates a string with a name and prints the output exactly as below (you can use your own name). Use f-strings in formatting your output and do not 'hard code' your program.")
#Exercise 7 uses range,length combines and f format

name = "Vrishab"

print(f'The string is "{name}".')

for i in range(len(name)):
    char = name[i]
    print(f'The character in position {i} is {char}')

