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
from _ast import While

'''s = "Bentley University, Waltham, MA"
result = ""
for ch in s:
    if ch.isupper():  # Check if the character is uppercase
        result += ch.lower()  # Convert uppercase to lowercase
    else:
        result += "-"  # Replace non-uppercase characters with "-"
print(result)'''

'''firstName = "Tom"
lastName = "Brady"
code = firstName[0:2] + lastName[1:2] + lastName[-1]
code = code.upper()
print(code)'''

'''age = int(input("How old are you: "))
if age < 3:
    print("You get in for free.")
elif age >= 3 and age < 13:
    print("Your ticket is $10.")
else:
    print("Your ticket is $15.")'''

'''firstName = input("Enter your first name: ")
first = firstName[0]
lastName = input("Enter your last name: ")
last = lastName
collegeName = input("Enter your college name: ")
collegeMascot = input("Enter your college mascot: ")
shortname = first + last + "@" + collegeMascot + "." + collegeName + ".edu"
print("Your email address is", shortname)'''

'''flavor = input("Enter flavor: V[V]anilla or C[C]arrot: ").upper()
peopleserving = int(input("How many people are you serving? "))

if flavor == "V":
    flavor = "vanilla"
    if peopleserving <= 14:
        cost = 8
        cake = "round"
        print(f"You need a {cake} {flavor} cake and costs ${cost:.2f}")
    elif peopleserving > 14 and peopleserving <= 20:
        cost = 18
        cake = "sheet"
        print(f"You need a {cake} {flavor} cake and costs ${cost:.2f}")
    else:
        print("You need more than one cake")
if flavor == "C":
    flavor = "carrot"
    if peopleserving <= 14:
        cost = 14
        cake = "round"
        print(f"You need a {cake} {flavor} cake and costs ${cost:.2f}")
    elif peopleserving > 14 and peopleserving <= 20:
        cost = 29
        cake = "sheet"
        print(f"You need a {cake} {flavor} cake and costs ${cost:.2f}")
    else:
        print("You need more than one cake")'''

'''ADDITIONAL = 10
FIRSTTHREE = 15
INNITIALHOURS = 3

hours = int(input("Enter the number of hours: "))

if hours <= 3:
    costtopark = hours * FIRSTTHREE
else:
    costtopark = FIRSTTHREE * INNITIALHOURS
    costtopark += (hours - INNITIALHOURS) * ADDITIONAL
print(f"The cost to park {hours} hours is ${costtopark:.2f}")'''

'''STEREOSYSTEM = 850.33
TELEVISION = 1274.90
print(f"Stereo System ${STEREOSYSTEM:.2f}")
print(f"Television ${TELEVISION:,.2f}")'''

'''word = input("Enter a word: ").lower()

for ch in word:
    if ch == 'a':
        word = word.replace(ch,'@')
    elif ch == 'e':
        word = word.replace(ch,'#')
    elif ch == 'i':
        word = word.replace(ch,'!')
    elif ch == 'o':
        word = word.replace(ch,'%')
    elif ch == 'u':
        word = word.replace(ch,'^')

print("The new word is: ", word)'''

'''donutsamount = int(input("How many donuts? "))

if donutsamount % 12 == 0:
    Dozen = donutsamount / 12
    print(f"{donutsamount} donuts is {Dozen:.0f} dozen donuts.")
else:
    Dozen = donutsamount // 12
    remainder = donutsamount % 12
    print(f"{donutsamount} donuts is {Dozen} dozen and {remainder} donuts.")'''

'''BOWLSMADE = 67565
John = .16 * BOWLSMADE
Jack = .47 * BOWLSMADE
Kyle = .09 * BOWLSMADE
Alex = .28 * BOWLSMADE

Star = 1000

newJohn = John // Star
newJack = Jack // Star
newKyle = Kyle // Star
newAlex = Alex // Star

print(f"John: {'*' * int(newJohn)}")
print(f"Jack: {'*' * int(newJack)}")
print(f"Kyle: {'*' * int(newKyle)}")
print(f"Alex: {'*' * int(newAlex)}")'''

'''i = 0
while i < 5:
    print(i)
    i += 1'''

'''FIRSTTHREE = 20
ADDITIONALHOURFIRSTDAY = 5
AFTERFIRSTDAY = 3

INITIALHOUR = 3
SECONDHOUR = 24
hours = int(input("Please enter the park hours: "))

if hours <= INITIALHOUR:
    print(f"The cost for {hours} hours is $20.")
elif INITIALHOUR < hours <= SECONDHOUR:
    cost = FIRSTTHREE + (hours - INITIALHOUR) * ADDITIONALHOURFIRSTDAY
    print(f"The cost for {hours} hours is $ {cost:.0f}.")
else:
    cost = FIRSTTHREE + (SECONDHOUR - INITIALHOUR) * ADDITIONALHOURFIRSTDAY + (hours - SECONDHOUR) * AFTERFIRSTDAY
    print(f"The cost for {hours} hours is $ {cost:.0f}.")'''

'''PARKING_CHARGES = 15

COST = int(input("Please enter the money you want to pay: "))

hours = COST // PARKING_CHARGES
remainder = COST % PARKING_CHARGES

print(f"You can park {hours:.1f} with {remainder:.1f} left.")'''

'''word = input("Please enter a string with 7 characters: ")

while len(word) != 7:
    word = input("Please enter a string with 7 characters: ")
print(f"The final string is {word[2:5].upper()}")'''

'''count = 6
for i in range(1,6):
    star = "*" * (count-i)
    print(star)'''

'''sum = 0
count = 0

while sum <= 100 and count < 5:
    count = count + 1
    number = float(input("Please enter a number: "))
    sum = sum + number


print(f"You entered {count} numbers and the total is {sum} ")'''

