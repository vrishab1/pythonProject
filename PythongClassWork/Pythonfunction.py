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
'''def printHello():
    print("Good Morning.")
    print("Have a happy sunny Day!")


def repeatprintHello(): 
    printHello()
    printHello()

repeatprintHello()'''

'''def printHello():
    saying = "Good morning" + "\nHave a great day!"
    return saying

text = printHello()
print(text)'''

'''def type_of_int(num):
    if num % 2 == 0:
        typ = 'even'
    else:
        typ = 'odd'
    return typ

num = int(input("Enter a number: "))
value = type_of_int(num)
print(f"The number {num} is {value}")'''

'''def print_hello(name):
    print(f"Good morning {name}")


print_hello("Samantha")
print_hello("David")
print_hello("Jason")
print("")'''

'''def add (a, b):
    print(f"s and b are: {a}, {b}")
    total = a + b
    return total

sumT = add(60,50)
print(f"Their sum is: {sumT}")
print(f"The sum is {add(50, 60)}")'''

'''
def temperature(celsius):
    fahren = (9 / 5) * celsius + 32
    return fahren

celsius = int(input("Enter Celsius temperature: "))
temp = temperature(celsius)
print(f"The Celsius temperature {celsius} is {temp} degrees")'''

'''def print_info(name, age):
    print(f"Name: {name}")
    print(f"Age: {age}")


print_info("Thomas", 23)
print_info(23, "Thomas")'''

'''
def print_info(name, age):
    print(f"Name: {name}")
    print(f"Age: {age}")


print_info(age=23, name="Thomas")
print_info(age=23, name="Sarah")
'''

'''def add(a=10, b=20):
    print(f"{a = } , {b = }")
    return a + b

total = add()
print(f"The sum is: {total}\n")
total = add(30)
print(f"The sum is: {total}\n")
total = add(60, 50)
print(f"The sum is: {total}\n")
total = add(b=50)
print(f"The sum is: {total}")'''

'''def print_info(numberfirst, numbersecond)
    print(f"First: {numberfirst}")
    print(f"Second: {numbersecond}")
   '''
'''
def print_number(numberfirst, numbersecond, numberthird):
    biggestnumber = max(numberfirst, numbersecond, numberthird)
    return biggestnumber

first_number = int(input("Enter a number: "))
second_number = int(input("Enter a number: "))
third_number = int(input("Enter a number: "))

biggestnumber = print_number(first_number, second_number, third_number)

print(f"The biggest number is: {biggestnumber}")
'''
'''def even_words(bunchOfwords):
    string2 = bunchOfwords.split()
    for word in string2:
        if len(word) % 2 == 0:
            print("Even string: {word}")

string1 = input("Enter a string: ")'''
'''
def arithmetic_sum(*nums):
    total = 0
    for x in nums:
        total += x
    return total

print(f"{arithmetic_sum(45, 32, 89, 78):.2f}")
print(f"{arithmetic_sum(880.95, 995.23, 345,150.263, 965.47):.2f}")
print(f"{arithmetic_sum(45.5, 32):.2f}")
print(f"{arithmetic_sum(45):.2f}")
print(f"{arithmetic_sum():.2f}")
'''
'''
def arith(num1, num2):
    total = num1+ num2
    diff = num1 - num2
    return total, diff

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
total1, diff1 = arith(num1, num2)

print(f"The total of the two numbers is {total1}")
print(f"The difference between the numbers is {diff1}")
'''

def new_func():
    global num
    num = num * 2
    print(f"Inside function: {num = }")

num = 75
new_func()
print(f"Outside function: {num = }")


