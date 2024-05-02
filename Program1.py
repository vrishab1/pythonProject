"""
Class: CS230--Section 3
Name: Vrishab Bharti
Description: Burger Bot - Program 1
(In this program you will simulate taking a customer’s order and calculating the amount of time required to prepare the burger.)

I pledge that I have completed the programming assignment
independently.
I have not copied the code from a student or any source.
I have not given my code to any student.
"""
#Time to produce each part of burger converted to seconds
BUNDROP = 6

TIMEFORTOPPINGS = 4

TIMEFORMELT = 45

#2.5 minutes converts to 150 seconds
TIMEFORHEAT = 150

COSTPERTOPPING = 0.33

COSTPERCHEESE = 0.50

TIMEFORTRAVEL = 27

#Welcome Customer to Burget Bot and tell them to fill out information for burger

print("Welcome to Burger Bot!")
print("Please enter details of your order.")

#Ask user to input name and toppings
name = input("\nPlease enter customer name: ")
sauce = int(input("Sauce? 1 for yes, 0 for no: "))
pickles = int(input("Pickles? 1 for yes, 0 for no: "))
tomatoes = int(input("Tomatoes? 1 for yes, 0 or no: "))
onion = int(input("Onion? 1 for yes, 0 for no: "))
lettuce = int(input("Lettuce? 1 for yes, 0 for no: "))
cheese = int(input("Cheese? 1 for yes, 0 for no: "))

# Time to produce each part of burger converted to seconds
TOTALTIMEFORTOPPINGS = TIMEFORTOPPINGS * (sauce + pickles + tomatoes + onion + lettuce + cheese)
TOTALTIMEFORMELTEDCHEESE = TIMEFORMELT * cheese

# Total time calculation
TOTALTIMESECONDS = BUNDROP + TOTALTIMEFORTOPPINGS + TOTALTIMEFORMELTEDCHEESE + TIMEFORHEAT + TIMEFORTRAVEL

# Minutes and seconds calculation
MINUTES = TOTALTIMESECONDS // 60
SECONDS = TOTALTIMESECONDS % 60

# Cost calculation
cost = 6.00 + COSTPERTOPPING * (pickles + tomatoes + onion + lettuce) + COSTPERCHEESE * cheese

#Outputs of all information entered in. Tells Cost and Time
print("\n" + name + ", your burger will be ready in " + str(TOTALTIMESECONDS) + " seconds, which is " + str(MINUTES) + " minutes and " + str(SECONDS) + " seconds.")

print("The cost is $" + str(cost))

print("Enjoy your burger!")
