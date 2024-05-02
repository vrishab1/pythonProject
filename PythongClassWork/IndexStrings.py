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
alist = ['accounting', 'economics', 'finance', 'management']
index2 = alist.index('economics')

alist = ['Apple', 'IBM', 'X', 'Facebook']
blist = [75785836, 463273217, 487775052, 43850938]
index1 = max(alist)
index2 = max(blist)

print(f"(The companies are {alist}")
print(f"Their earnings are {blist}")
print(f"The company with the highest earnings is {index1} with earnings of ${index2:,.2f}")


alist = ['accounting', 'management', 'finance', 'economics']
alist.sort()
print(f"The list is sorter in ascending order {alist}")

alist = ['accounting', 'management', 'finance', 'economics']
alist.sort(reverse=True)
print(f"The list is sorted in descending order {alist}")

alist = ['accounting', 'management', 'finance', 'economics']
alist.sort(key=len)
print(f"The list sorted by length is {alist}")

alist = ['accounting', 'management', 'finance', 'economics']
alist.sort(key=len, reverse=True)
print(f"sorted list according to length, reverse order: {alist}")

#This one does not work as you cannot sort characters of two different types


alist = ['apple', 'banana', 'kiwi', 'organge', 'grapefruit', 1,3,4]
alist.sort()
print(f"\nThe list sorted in ascending order is {alist}")

alist = [1,2,3,4]
blist = alist.copy()
print(f"alist is composed of {alist}")
print(f"blist is composed of {blist}")

alist[1] = 25
print()
print(f"\nalist is composed of {alist}")
print(f"\nblist is composed of {blist}")

'''
'''
alist = [4, 23, 9, 10, 33, 90]
clist = [10, 20, 60, 70, 100]
print(f"The list, alist, is {alist}")
print(f"The list, clist is {clist}")


result = []
dlist = list(zip(alist, clist))
print(dlist)

for item1, item2 in zip(alist, clist):
    result.append(item1 + item2)
print(f"The totals of the respective elements in the lists are {result}")
'''
'''
alist = ['debt', 'credit', ['bond', 'stock', ['note', 'wage']], 'price', 'tax']
print(f"alist[2] is {alist[2]}")
print(f"alist[2][1] is {[alist[2][1]]}")
print(f"alist[2][1][2] is {[alist[2][1][2]]}")
'''
'''
alist = ['debit', ['stock', 'bond',], 'credit']
print(f"The original list is {alist}")
alist[1][1] = "tax"
print(f"The updates list is {alist}")
alist.insert(0, 'price')
print(f"The original list is {alist}")
alist[1].extend(['price', 'tax'])
print(f"The updates list is {alist}")
'''

alist = ['debit', ['stock', 'bond',], 'credit']
print(f"The original list is {alist}")

del alist[1][1]
print(f"The updated list is {alist}")

alist[1].remove("stock")
print(f"The updates list with removed is {alist}")

print(f"The length of alist is {len(alist)}")
print(f"The length of the alist is {len(alist[1])}")

alist = [[1,2,3],[4,5,6],[7,8,9]]
for number in alist:
    print(number)


