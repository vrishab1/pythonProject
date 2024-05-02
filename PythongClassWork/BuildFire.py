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
command = "build fire"
[action, object] = command.split()

match (action, object):
    case ("build", "fire"):
        print("Building a fire")
    case _:
        print("Unknown command")