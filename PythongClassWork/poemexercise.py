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

fhand = open('poem.txt', 'r+')
lines = fhand.read()
fhand.write("Second version of poem\n")
fhand.write(lines)
fhand.close()

'''
print("\nDemonstration of Simultaneous Read and Write")
fhand = open('poem.txt', 'r')
for line in fhand:
    line = line.rstrip()
    print(line)
'''
'''
file = open('poem.txt', 'a')
c=input("Enter string to append: ")
file.write(c + '\n')
file.close()

print("Contents of appended file:")
with open('poem.txt') as file:
    for line in file:
        line = line.rstrip()
        print(line)
        '''