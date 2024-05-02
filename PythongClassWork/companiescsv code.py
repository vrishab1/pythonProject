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

FILENAME = ("companies.csv")
company = []
exec = []
since = []

fhand = open(FILENAME)
for line in fhand:
    line = line.rstrip().split(",")
    print(line)
    if line[0] == "Company":
        continue
    else:
        company.append(line[0])
        exec.append(line[1])
        year = int(line[2])
        since.append(year)

print(f"\nThe companies are: \n{company}\n")
print(f"\nThe executives are: \n{exec}")
print(f"\nThe years since they took the helm are:\n")
