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
first = input("Enter your first name: ")
firstName = [0]
second = input("Enter your second name: ")
lastName = second.lower()
college = input("Enter your college name: ")
collegeName = str(college)
collegemascot = input("Enter your college mascot: ")
mascotName = str(collegemascot)

email = str(firstName) + str(lastName) + "@" + mascotName + "." + collegeName + ".edu"

print("Your email address is: ", email)


