"""
Class: CS230--Section 3
Name:
Description: Quiz #1 Spring 2024

I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student.
"""

print(f"{15 * '='}Question 1{15 * '='}")
# your code for Question 1 fills in the two functions and how they are called

def shortname(first_name, last_name):
    if len(last_name) > 5:
        short_last_name = last_name[:5]
    else:
        short_last_name = last_name
    return f"{first_name[0]}{short_last_name}".upper()

def print_short(name, short):
    print(f"{name[0]} {name[1]:<20}Shortname: {short}")

name1 = ('Jimmy', 'Kimmel')
short_name1 = shortname(name1[0], name1[1])
print_short(name1, short_name1)

name2 = ('Chris', 'Rock')
short_name2 = shortname(name2[0], name2[1])
print_short(name2, short_name2)


print(f"\n{15 * '='}Question 2{15 * '='}")

reviews = [["Jerry Oh", 5, "Amazing stay!"],
           ["Quentin Gonza", 4, "Great location."],
           ["Max Jones", 1, "Bedbugs in my room!"]
           ]

# your code for Question 2 goes here


print(f"\n{15 * '='}Question 3{15 * '='}")

rooms = {
    "single": {"available": 10, "price": 150},
    "double": {"available": 20, "price": 200},
    "suite": {"available": 5, "price": 400}
}

total_rooms_available = sum(room["available"] for room in rooms.values())

max_price = 0
expensive_room_type = ""

for room_type, details in rooms.items():
    if details["price"] > max_price:
        max_price = details["price"]
        expensive_room_type = room_type

print(f"The total rooms available is: {total_rooms_available}")
print(f"The most expensive room is a {expensive_room_type} with a price of ${max_price:.2f}")

print(f"\n{12 * '=':13s}Quiz Completed{12 * '=':>13s}")
