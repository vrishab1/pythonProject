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
'''small_numbers = [1,2,3,4]
numbers = []
for j in small_numbers:
    numbers.append(j*2)
print(numbers)
'''

small_numbers = [1,2,3,4]
numbers = [j * 2 for j in small_numbers]
print(numbers)

sampleDict = [{"name": "Joe", "email": "joe@some.com", "orders": 8},
              {"name": "Mary", "email": "mary@some.com", "orders": 10},
              {"name": "Jorge", "email": "jorge@some.com", "orders": 6},]

for key in sampleDict:
    print(f"Name: {key["name"]}, Email: {key["email"]}")

def sortedList(alist):
    xlist = []
    for i in alist:
        if i[0] == 'x':
            xlist.append(i)
            alist.remove(i)
    xlist.sort()
    alist.sort()
    newlist = xlist + alist
    return newlist


alist = ['mix', 'xyz', 'apple', 'xanadu', 'aardvark', 'xander', 'blueberry']
print(f"The original list is {alist}")
newList = sortedList(alist)
print(f"The new list is {newList}")

weather = {"Monday": [50, 38],
           "Tuesday": [55, 64],
           "Wednesday": [52, 45],
           "Thursday": [52, 54],
           "Friday": [46, 67]}

days = []
temps = []
for x in weather:
    lowTemp = min(weather[x])
    days.append(x)
    temps.append(lowTemp)

lowestTemp = min(temps)
tempIdex = temps.index(lowestTemp)
lowestDay = days[tempIdex]
print(f"The coldest day is {lowestDay} with a temperature of {lowestTemp} degrees")

alist = []
loop = True
while loop:
    num = input("Enter a number [blank to quit]: ")
    if num == '':
        loop = False
    else:
        num = int(num)
        alist.append(num)

neglist = []
poslist = []
zerolist = []
for i in range(len(alist)):
    if alist[i] < 0:
        neglist.append(alist[i])
    elif alist[i] > 0:
        poslist.append(alist[i])
    else:
        zerolist.append(alist[i])

newList = neglist + zerolist + poslist
newList1 = [str(newList[i]) for i in range(len(newList))]
print(" ".join(newList1))
