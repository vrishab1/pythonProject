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

def printHello():
    print("Good morning.")
    print("Have a great day!")


printHello()

def add(a=10, b=20):
    print(f"{a = }, {b = }")
    return a + b


total = add()
print(f"The sum is: {total}\n")

total = add(30)
print(f"The sum is: {total}\n")

total = add(60, 50)
print(f"The sum is: {total}")

print("Exercise #1")
def arithmetic_sum(*nums):
    total = 0
    for x in nums:
        total += x
    return total


print(f"{arithmetic_sum(45,32,89,78):.2f}")
print(f"{arithmetic_sum(880.95,995.23,345,150.263,965.47):.2f}")
print(f"{arithmetic_sum(45.5,32):.2f}")
print(f"{arithmetic_sum(45):.2f}")
print(f"{arithmetic_sum():.2f}")

print("\nExercise #2")
def largest(x,y,z):
    if (x > y) and (x > z):
        largest = x
    elif (y > x) and (y > z):
        largest = y
    else:
        largest = z
    return largest


num1 = float(input("Enter a number: "))
num2 = float(input("Enter a number: "))
num3 = float(input("Enter a number: "))
print("The largest number is",largest(num1,num2,num3))


print("\nExercise #3")
def sumNumbers(*args):
    product = 1
    for i in args:
        print(i)
        if i == 0:
            product = 0
        else:
            product += i
    return product


print(f'The total of (1,2,3) is {sumNumbers(1,2,3)}')
print(f'The total of (45,65) is {sumNumbers(45,65)}')
print(f'The total  is {sumNumbers(0)}')


