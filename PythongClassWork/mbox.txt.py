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
fhand = open("mbox.txt")
print(fhand)
fhand.close()
'''
'''
fhand  = open("mbox.txt")
inp = fhand.read()
print("Contents of file mbox.txt from read()")
print(inp)
print("Number of characters in the file is", len(inp))
print("First 20 characters in the file is", inp[:20])
'''

'''
print("\nAnother use of readline()")
fhand = open("mbox.txt")
loop = True
while loop:
    line = fhand.readline().rstrip()
    if line != " ":
        print(f"Line: {line}")
    else:
        loop = False
'''

'''
fhand = open("mbox.txt")
lines = fhand.readlines()
print("\nResult of readline() -> a list ")
print(lines)
print("\nConverting the list to strings")
for line in range(len(lines)):
    sentence = lines[line].rstrip()
    print(f"\t{sentence}")
    '''
'''
print("Easiest way to read in lines from a file")
fhand = open("mbox.txt")
for line in fhand:
    line = line.rstrip()
    print(f"\t{line}")
'''