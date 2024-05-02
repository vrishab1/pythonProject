"""
Class: CS230--Section 3
Name: Vrishab Bharti
Description: Quiz #1 Spring 2024

I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student.
"""

print(f"{15*'='}Question 1{15*'='}")
SERVICEPLANBASIC = "Basic"
SERVICEPLANPLUS = "Plus"
SERVICEPLANULTRA = "Ultra"
PRICEBASIC = 7.99
PRICEPLUS = 10.99
PRICEULTRA = 14.99

serviceplan = input("Enter the service code [B]asic, [P]lus, [U]ltra: ").lower()
if serviceplan == "b":
    serviceplan = SERVICEPLANBASIC
    PRICE = PRICEBASIC
    service = 'valid'
elif serviceplan == "p":
    serviceplan = SERVICEPLANPLUS
    PRICE = PRICEPLUS
    service = 'valid'
elif serviceplan == "u":
    serviceplan = SERVICEPLANULTRA
    PRICE = PRICEULTRA
    service = 'valid'
else:
    service = "invalid"
    print("The service code is invalid.")

if service != 'invalid':
    print(f"You have selected the {serviceplan} which costs ${PRICE:.2f} per month.")


'''print(f"\n{15*'='}Question 2{15*'='}")
# your code for Question 2 goes here
mystery = 'He12llo, Py00th55on!'

print(f"The original string is {mystery}")
newmystery = mystery.replace()
'''
print(f"\n{15*'='}Question 3{15*'='}")
# your code for Question 3 goes here
WEEKDAYPRICE = 1.25
WEEKENDPRICE = 1.00

for i in range (4,37, 4):
    weekdaycost = i * WEEKDAYPRICE
    weekendcost = i * WEEKENDPRICE
    print(f"For {i:2} cookies: Weekday cost: ${weekdaycost:5.2f}, Weekend cost: ${weekendcost:5.2f}")


print(f"\n{12*'=':13s}Quiz Completed{12*'=':>13s}")

