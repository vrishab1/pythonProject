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
alist = ['accounting', 'finance']
blist = [100, 250.75]
clist = [*alist, *blist]
print('The origin alist is: ', alist)
print('The origin blist is: ', blist)
print('The rules of concatenatig the list are ', clist)'''

'''
alist = ['accounting', 'finance']
print("The list alist repeated two times is", alist * 2)'''
'''
alist = ['accounting', 'finance', 'marketing', 'economics', 'management']
length = len(alist)

print(f"The length of list {alist} is {length}")

alist1 = alist[1:4]
print(f"The elements at indiciates 1, 2, 3 are {alist}")
alist1 = alist[1:-1]
print(f"The elements starting at index 1 andup to 1 from the end are {alist1}")
alist1 = alist[:3]
print(f"The elements from index - to index 2 are {alist1}")
alist1 = alist[2:]
print(f'The elements from index 2 to the end are {alist1}')
alist1 = alist[0:3:2]
print(f"Every other element from index 0 to index 2 are {alist1}")
'''
'''
alist = [10 ,20, 30, 40, 50, 60, 70, 80, 90, 100]
print(f"The original list is {alist}")
length = len(alist)
number = int(input("Enter a number between 0 and 10: "))
sub1 = alist[:number]
sub2 = alist[-number:]
print("The substring of the list between 0 and", number, "is", sub1)
print("The substring of the list between the end of the list and", number,"is", sub2)
'''
'''
alist = ['accounting', 'finance']
print(f"The original list is {alist}")
alist.append("marketing")
print(f"\nThe new list is {alist}")

alist = ["accounting", "finance"]
blist = ["economics", 'management']
alist.extend(blist)
print(f"The new list is {alist}")

alist = ["accounting", "finance"]
alist.insert(1,"economics")
print(f"The new list is {alist}")
alist.insert(3, "management")
print(f"The new list is {alist}")
'''
'''
randomnumbers = []

element = int(input("Enter number of elements: "))

for i in range(element):
    randnum = random.randint(1, 500)
    randomnumbers.append(randnum)

print(randomnumbers)
'''
'''
alist = ["accounting", "economics", "finance", "management", "finance"]
print(f"The original list is {alist}")
alist.remove("finance")
print(f"The new list is {alist}")

item = alist.pop(1)
print(f'The item removed is "{item}"')
print(f"The new list is {alist}")

del(alist[1])
print(f"The new list is {alist}")
'''
'''
numbers = [10, 15, 20, 25, 30, 35, 40, 45, 50]
x = 25
print(x in numbers)
y = 27
print(y in numbers)

string = "Python Programming"
if "Python" in string:
    print("Great!")
else:
    print("Python not in string")
    '''

'''alist = ["accounting", "economics", "finance", "management"]
index1 = alist.index("economics", 2, 3)
print(f"The index of the topic economics using start and stop is {index1}")
'''
'''
alist = [[1,2,3],[4,5,6], [7,8,9]]


print(f"The original list {alist}")
newlist = alist.remove("[")
print(f"The flattened list is {newlist}")
'''


'''
alist = [[1,2,3], [4,5,6], [7,8,9]]

diagonal_sum = sum(alist[i][i] for i in range(len(alist)))

print(f"The sum of the diagonal elements of the list {alist} is {diagonal_sum}")



blist = [[4,1,6], [7,8,5], [4,10,8]]
random_num = random.choice([blist[i][i] for i in range(len(blist))])


print(f"A random value from the list is {random_num}")
'''

'''
###Most likely ot be question on quiz
alist = []
for n in range(10):
    alist.append(n)
print(f"The list is {alist}")

blist = [n for n in range(10)]
print(f"The list from list comprehension is {blist}")

alist = [10, 20, 30]
print(f"The list is {alist}")

blist = [num * 3 for num in alist]
print(f"The list from list comprehension is {blist}")

alist = [num for num in range(31) if num % 3 == 0]
print(f"The list is {alist}")


string = eval(input("Enter a series of numbers, separated by commas: "))
print(string)
alist = list(string)
print(f"The list is {alist}")

print()
string = input("Enter a series of numbers, separated by spaces: ")
print(f"The numbers that were inputted are '{string}'")
items = string.split()
print(f"The items in a list are {items}")
blist = [float(x) for x in items]
print(f"The list is {blist}")

'''
alist = [1, 2, 3, 4]
for i in alist:
    alist.append("emp")

print(alist)


