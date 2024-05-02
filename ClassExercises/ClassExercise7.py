"""
Class: CS230--Section 3
Name: Vrishab Bharti
Description:
Exercise 1: Write a program that asks the user for the file name and counts the number of words in that file. Please create a file.
Exercise 2: Use the file, Alice.txt, read it in and then write all of the five-letter words it contains to another file. Your words can include punctuation within the words but should not include "external" punctuation. For extra credit of two points, find all words that do not include punctuation within the word.
Exercise 3: Write a program that asks the user for the name of a file and prints all the numbers present in the text file.
Exercise 4: Write a program that asks the user to enter the name of two text files and compares them.  Create two text files that are similar but differ on a single line. Output a message stating the files are the same or display the first line number and corresponding line of each file that is different.
Exercise 5: Add option 3 to managefiles.py  that lists each file in a specified (or the current) directory, and then prints out the total size of the files in that directory. Include this exercise in the same Python file as the previous four programs, if you do it.
I pledge that I have completed the programming assignment
independently.
I have not copied the code from a student or any source.
I have not given my code to any student.
"""

print("\nExercise 1: Write a program that asks the user for the file name and counts the number of words in that file. Please create a file.\n")
##Uses def, input, reading a file, spliting the lines and lengths

def count_words_in_file():

    number_of_words = 0

    fname = input("Enter file name: ")

    with open(fname, 'r') as f:
        data = f.read()
        lines = data.split()
        number_of_words += len(lines)

    print(f"Number of words: in {fname} is {number_of_words}")

count_words_in_file()

print("\nExercise 2: Use the file, Alice.txt, read it in and then write all of the five-letter words it contains to another file. Your words can include punctuation within the words but should not include 'external' punctuation. For extra credit of two points, find all words that do not include punctuation within the word.\n")
##Uses openining a read only file, dictionary, splitting words, making each word that is within 5 characters combine, appending, opens file in write mode

with open("Alice.txt", "r") as f:

    words_Dict = []

    for line in f:
        line_words = line.split()
        for i in line_words:
            Permissable_word = ''.join([char for char in i if ('a' <= char <= 'z' or 'A' <= char <= 'Z')])
            Permissable_word = Permissable_word.lower()
            if len(Permissable_word) == 5:
                words_Dict.append(Permissable_word)

with open("FiveLetterWords.txt", "w") as k:
    for i in words_Dict:
        k.write(i + "\n")

print("File FiveLetterWords.txt has been written")

print("\nExercise 3: Write a program that asks the user for the name of a file and prints all the numbers present in the text file.\n")
##Uses read only files where the lines are split and only the digit values are printed

fname = input("Enter file name: ")
print(f"The numbers in file {fname} are: ")

with open(fname, 'r') as f:
    for line in f:
        words = line.split()
        for i in words:
            for letter in i:
                if (letter.isdigit()):
                    print(letter)

print("\nExercise 4: Write a program that asks the user to enter the name of two text files and compares them.  Create two text files that are similar but differ on a single line. Output a message stating the files are the same or display the first line number and corresponding line of each file that is different.\n")
##Opens file1 and file2 as read only, loops, Boolean, reading lines from both files

def comparing_files(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        line_number = 1
        files_same = True

        while True:
            line1 = f1.readline()
            line2 = f2.readline()

            if not line1 and not line2:
                break

            if line1 != line2:
                files_same = False
                print(f"\nFiles differ at line {line_number}:")
                print(f"Text from {file1}: {line1.strip()}")
                print(f"Text from {file2}: {line2.strip()}")

            line_number += 1

        if files_same:
            print("\nThe files are the same.")
        else:
            print("\nNo more differences.")

file1 = input("Enter the name of the first file: ")
file2 = input("Enter the name of the second file: ")
comparing_files(file1, file2)



