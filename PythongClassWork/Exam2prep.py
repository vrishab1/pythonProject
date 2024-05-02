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

##Short answer examples

##Short answer 1
##Original
small_numbers = [1,2,3,4]
numbers = []
for i in small_numbers:
    numbers.append(i * 2)
print(numbers)

##Rewritten in list comprehension
small_numbers = [1,2,3,4]
new_numbers = [i * 2 for i in small_numbers]
print(new_numbers)

##Short answer 2
sampleDict = [{"name": "Joe", "email": "joe@some.com", "orders": 8},
              {"name": "Mary", "email": "mary@some.com", "orders":10},
              {"name": "Jorge", "email": "jorge@some.com", "orders":6}]

all_SampleDict = []

for sample in sampleDict:
    print(f"Name: {sample["name"]}, Email: {sample["email"]}")

##Practice 1:

string_list = ["mix", "xyz", "apple", "xanadu", "aardvark", "xander", "blueberry"]

def x_first(string):
    if string.startswith('x'):
        return (0, string)
    else:
        return (1, string)

sorted_list = sorted(string_list, key=x_first)

print(sorted_list)

##class answer

def sortedList(alist):
    xlist = []
    for i in alist:
        if i[0] == "x":
            xlist .append(i)
            alist.remove(i)
    xlist.sort()
    alist.sort()
    newlist = xlist + alist
    return newlist

alist = ["mix", "xyz", "apple", "xanadu", "aardvark", "xander", "blueberry"]
print(f"The original list is {alist}")
newList = sortedList(alist)
print(f"The new list is {newList}")

##Practice 2:

weather = {"Monday": [50, 38],
           "Tuesday": [55, 64],
           "Wednesday": [52, 45],
           "Thursday": [52, 54],
           "Friday": [46, 67]}

temps = []
days = []
for key in weather:
    lowTemp = min(weather[key])
    days.append(key)
    temps.append(lowTemp)

lowestTemp = min(temps)
tempIdex = temps.index(lowestTemp)
lowestDay = days[tempIdex]
print(f"The coldest day is {lowestDay} with a temperature of {lowestTemp}")


##Practice 4
gadgets = ["Mobile", "Laptop", 100, "Camera", 310.28, "Speakers", 27.00, "Television", 1000, "Laptop Case", "Camera Lens"]

String_items = [i for i in gadgets if i is str]

print(String_items)






