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
tup1 = 'business', 'finance', 'accounting'
print(f'The string is a tuple: {tup1}')
tup2 = ("business", "finance", "accounting")
print(f"The tuple is {tup2}")

tup1 = ("accounting",)
print(f"The tuple: {tup1}")
tup2 = ("accounting")
print(f"The string: {tup2}")
tup3 = tuple()
print(f"The empty tuple is {tup3}")
tup4 = tuple('business')
print(f"This is a tuple from the word 'business' {tup4}")

tup = ('business', 'finance', 'accounting')
print(f"The zero-th element of the tuple is {tup[0]}")
print(f"The elements 1 through 2 of the tuple are {tup[1:3]}")
print(f"The last element of the tuple is {tup[-1]}")

tup = ('business', 'finance', 'accounting')
tup1 = (1,2,3)
for n,m in zip(tup, tup1):
    print(f"{n = }, {m = }")
    
tup = ("business", "finance", "accounting", "finance")
print(f"Is any element of the tuple True? {any(tuple)}")
print(f"The number of times 'finance' appears: {tup.count("finance")}")
print(f"The smallest major: {min(tup)}")
print(f"The largest major: {max(tup)}")
print(f"The length of the tuple: {len(tup)}")

numbers = (1, 2, 3, 4)

'''
'''
dict1 = {}
print(f"An empty disctionary {dict1}")
dict2 = {1: 'finance', 2: 'accounting', 3: 'economics'}
print(f"A dictionary with integer keys {dict2}")
dict3 = {"name": "john" : "age", 21, "year": "sophmore"}
'''

dict1 = {1: "finance", 2: "accounting", 3: "economics"}
print(f"The dictionary is {dict1}")
print(dict1[2])
print(f"dict1[1] = {dict1[1]}")

dict2 = {"name": "John", "age" : 21, "year": "sophomore"}
print(f"The dictionary is {dict2}")
print(f"Name: {dict2['name']}")

dict1 = {1: "finance", 2: "accounting", 3: "economics"}
print(f"The original dictionary is {dict1}")
dict1[4] = "marketing"
print(f"The updated dictionary is {dict1}")
dict1[1] = "math"
print(f"The updated dictionary is {dict1}")

dict1 = {1: "finance", 2: "accounting", 3: "economics"}
print(f"The original dictionary is {dict1}")
for val in dict1:
    dict1[val] = dict1[val] + "0" + str(val)
print(f"The updated dictionary is {dict1}")



