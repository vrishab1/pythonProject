"""
Class: CS230--Section 3
Name: Vrishab Bharti
Description:
Exercise 1: Write a Python function that takes a total taxable purchase as an argument and a default argument of the value of the sales tax. In the function, calculate and return the sales tax amount rounded to decimal places. Use the Massachusetts sales tax rate of 6.25%.
Exercise 2: Write a Python function that accepts a string and calculates the number of upper-case letters and lower-case letters. The running of the script would look as follows:
Exercise 3: Write a function that takes a distance and fuel costs as a required argument and mpg with a default of 50 mpg (functions without these three parameters will not be acceptable solutions!). The program asks the user for the distance and fuel costs and the function should return the cost in dollars. Format the output using f-strings. The output would look like the following:
Exercise 4: Write a function that takes two strings and determines whether they are an anagram. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. Spaces are counted in the phrase. The running of the script would look as follows, meaning pass to the function the two strings in each example (please include these strings in your code so as to eliminate user input):
Exercise 5: You are driving a little too fast, and a police officer stops you. Write a function that computes the result, encoded as an integrer value: 0=no ticket, 1=small ticket, 2=big ticket. If your speed is 60 or less, the result is 0. If your speed is between 61 and 80 inclusive, the result is 1. If speed is 81 or more, the result is 2. Unless it is your birthday -- on that day, your speed can be 65 higher and you will not get a ticket. The result of the function would be as follows (please include these strings in your code so as to eliminated user input) :

I pledge that I have completed the programming assignment
independently.
I have not copied the code from a student or any source.
I have not given my code to any student.
"""


print('\nExercise 1: Write a Python function that takes a total taxable purchase as an argument and a default argument of the value of the sales tax. In the function, calculate and return the sales tax amount rounded to decimal places. Use the Massachusetts sales tax rate of 6.25%.')
#Uses define and f statements as well as multiplication

def calculate_sales_tax(total_taxable_purchase, sales_tax_rate=0.0625):
    sales_tax_amount = total_taxable_purchase * sales_tax_rate
    print(f"Sales tax due: ${sales_tax_amount}")

total_taxable_purchase = float(input("Purchase amount: "))

calculate_sales_tax(total_taxable_purchase)

print("\nExercise 2: Write a Python function that accepts a string and calculates the number of upper-case letters and lower-case letters.")
#Uses define and f statements as well as lowercase and uppercase, if else statements, and increment increase statements

def count_of_string(string_used):
    upper_case_count = 0
    lower_case_count = 0

    for char in string_used:
        if char.isupper():
            upper_case_count += 1
        elif char.islower():
            lower_case_count += 1

    print(f"No. of Upper-Case characters: {upper_case_count}")
    print(f"No. of Lower-Case characters: {lower_case_count}")

string_used = input(f"Enter a string: ")
count_of_string(string_used)


print("\nExercise 3: Write a function that takes a distance and fuel costs as a required argument and mpg with a default of 50 mpg (functions without these three parameters will not be acceptable solutions!). The program asks the user for the distance and fuel costs and the function should return the cost in dollars. Format the output using f-strings. ")
#Uses define and f statements as well as multiplication and division and round to 2nd decimal

def cost_to_travel(distance_traveled, cost_per_gallon, mpg=50):
    total_cost = (distance_traveled/mpg) * cost_per_gallon
    print(f"The cost to travel {distance_traveled:.2f} miles when the cost per gallon is ${cost_per_gallon:.2f} is ${total_cost:.2f}.")

distance_traveled = float(input(f"Enter distance traveled: "))
cost_per_gallon = float(input(f"Enter cost per gallon: "))
cost_to_travel(distance_traveled, cost_per_gallon)

print("\nExercise 4: Write a function that takes a distance and fuel costs as a required argument and mpg with a default of 50 mpg (functions without these three parameters will not be acceptable solutions!). The program asks the user for the distance and fuel costs and the function should return the cost in dollars. Format the output using f-strings.")
#Uses define and f statements as well as equal to and not equal to and sorted function

def anagram_or_not(string1, string2):
    if sorted(string1) == sorted(string2):
        print(f"'{string1}' and '{string2}' are anagrams.")
    elif sorted(string1) != sorted(string2):
        print(f"'{string1}' and '{string2}' are not anagrams.")

anagram_or_not("debit card", "bad credit")
anagram_or_not("dirty room", "dormitory")


print("\nExercise 5:You are driving a little too fast, and a police officer stops you. Write a function that computes the result, encoded as an integrer value: 0=no ticket, 1=small ticket, 2=big ticket. If your speed is 60 or less, the result is 0. If your speed is between 61 and 80 inclusive, the result is 1. If speed is 81 or more, the result is 2. Unless it is your birthday -- on that day, your speed can be 65 higher and you will not get a ticket. The result of the function would be as follows (please include these strings in your code so as to eliminated user input)")
#Uses define and f statements as well as if else functions

def caught_speeding(speed, is_birthday):
    ticket = 0
    if is_birthday:
        if speed <= 65:
            ticket = 0
    else:
        if speed <= 60:
            ticket = 0
        elif 61 <= speed <= 80:
            ticket = 1
        else:
            ticket = 2

    print(f"caught_speeding({speed},{is_birthday}) → {ticket}")


caught_speeding(60,False)
caught_speeding(65,False)
caught_speeding(65,True)


















