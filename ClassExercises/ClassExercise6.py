"""
Class: CS230--Section 3
Name: Vrishab Bharti
Description:
Exercise 1: Write a program to take a string and create a dictionary with the key as the first character and the value as words starting with that character
Exercise 2: With the following two lists, which match up, so Alice’s age is 20, Bob’s age is 21, and so on. Write a program that combines these lists into a dictionary. The key would be the age and the value would be the name, so keys can have multiple values and would look like this:
Exercise 3: Given the following dictionary of course and the professors that teach those courses. Display the professors in alphabetical order from A to Z and then find the professor with the longest name.
Exercise 4: Write a function with three parameters: a dictionary of keys that are user names  and with values that are the passwords for those user names, username which is the login name, and password which is the password for the user name. The function should return True if the user exists and the password is correct and False otherwise. Create your own dictionary.

I pledge that I have completed the programming assignment
independently.
I have not copied the code from a student or any source.
I have not given my code to any student. 
"""
print("\nExercise 1: Write a program to take a string and create a dictionary with the key as the first character and the value as words starting with that character\n")
##Uses def and for and if else functions and split. Also creates a Dict
def dict_from_string(input_string):
    words = input_string.split()
    string_dict = {}
    for i in words:
        first_char = i[0]
        if first_char not in string_dict:
            string_dict[first_char] = [i]
        else:
            string_dict[first_char].append(i)

    for letter in string_dict:
        print(f"{letter}: {string_dict[letter]}")

input_string = input("Enter a string: ")
dict_from_string(input_string)


print("\nExercise 2: With the following two lists, which match up, so Alice’s age is 20, Bob’s age is 21, and so on.  Write a program that combines these lists into a dictionary. The key would be the age and the value would be the name, so keys can have multiple values\n")
##Uses dictionary, for loop, enumerate, if else loops, and append.

names = ['Alice', 'Bob', 'Cathy', 'Dan', 'Ed', 'Frank', 'Gary', 'Helen', 'Irene', 'Jack', 'Kelly', 'Larry']
ages = [20, 21, 18, 18, 19, 20, 20, 19, 19, 19, 22, 19]

age_name_dict = {}

for i, name in enumerate(names):
    age = ages[i]
    if age not in age_name_dict:
        age_name_dict[age] = [name]
    else:
        age_name_dict[age].append(name)

print(age_name_dict)

print("\nExercise 3: Given the following dictionary of course and the professors that teach those courses. Display the professors in alphabetical order from A to Z and then find the professor with the longest name.\n")
##Uses dict, for, sorted, if, extend, and join functions

professors = {"CS230": ["Bernstein", "Jones", "Prentice"],
 "CS150": ["Ganfield", "Sullivan", 'Connors'],
 "CS213": ["Sinema", "McSally"],
 "CS350": ["Feinstein", "Loudermilk"]}

all_professors_Dict = []

for i in professors:
    all_professors_Dict.extend(professors[i])

sorted_names = sorted(all_professors_Dict)

longest_name = ' '

for name in sorted_names:
    if len(name) > len(longest_name):
        longest_name = name

sorted_names_str = ', '.join(sorted_names)
print(f"The list of names sorted is {sorted_names_str}")
print(f"The longest name is {longest_name}")

print("\nExercise 4:Write a function with three parameters: a dictionary of keys that are user names and with values that are the passwords for those user names, username which is the login name, and password which is the password for the user name. The function should return True if the user exists and the password is correct and False otherwise.\n")
##Uses def, if else, dict, and Boolean
def login(users_dict, username, password):
    if username in users_dict and users_dict[username] == password:
        print("The dictionary of users and passwords is", users_dict)
        print("The login was successful\n")
    else:
        print("The dictionary of users and passwords is", users_dict)
        print("login failed...\n")

user_dict = {'vbharti': 'Bharti1', 'SBharti': 'Bharti2', 'MRani': 'Rani1!'}

login(user_dict, 'vbharti', 'Bharti1')
login(user_dict, 'vbharti', 'Bharti2')


