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
fname = input("Enter the file name: ")
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith("Subject:"):
        count = count + 1
print("There were", count, "subject lines in", fname)
fhand.close()
'''
'''
fout = open('output.txt', 'w')
line1 = "We are learning how to write\n"
fout.write(line1)
line2 = "to text files in Python\n"
fout.write(line2)
fout.close()

fhand = open("output.txt")
print("Output of Write function is ")
for line in fhand:
    line = line.rstrip()
    print(line)
    '''
'''
import random
f = open("integers.txt", 'w')
for count in range(500):
    number = random.randint(1, 500)
    f.write(str(number) + '\n')
    f.write(f"{str(number)}\n")
f.close()

print("The numbers in the file are: ")
f = open("integers.txt")
for line in f:
    line = line.rstrip()
    print(line)
    '''

import random
with open("integers.txt", 'w') as f:
    for count in range(10):
        number = random.randint(1, 500)
        f.write(str(number) + '\n')

print("The numbers in the file are: ")
f = open("integers.txt")
for line in f:
    line = line.rstrip()
    print(line)