"""
Class: CS230--Section 3
Name: Vrishab Bharti
Description: Burger Bot - Program 2
(In this program you will simulate taking a customer’s order and calculating the amount of time required to prepare the burger with the improved process.)

I pledge that I have completed the programming assignment
independently.
I have not copied the code from a student or any source.
I have not given my code to any student.
"""
# Burger Bot Ordering System pt 2
# Date: 3/04/2024
# Description: This program facilitates customer orders for standard and customized burgers, computes total cost and time.

#Time to produce each part of burger converted to seconds as well as cost
BUN_TIME = 6
STATION_TRAVEL_TIME = 3
TOPPING_TIME = 4
MELTING_TIME = 45
ADDITIONAL_TIME = 70
BURGER_COOK_TIME = 60
BASE_COST = 6
CHEESE_COST = 0.50
BURGER_PRICE = 7.82
ADDITIONAL_FEE_7TO10 = 0.50
ADDITIONAL_FEE_11TO12 = 0.75
MAX_STANDARD_BURGERS = 10

#Initializing Variables and Boolean functions
total_burgers_standard = 0
total_burgers_customized = 0
total_cost = 0
order_cost = 0
master_total_time = 0
additional_fee = 0
redirected_to_custom = False
burger_choice = ''

#Greeting customer and asking for name
print("Welcome to Burger Bot")
customer_name = input("\nCustomer name: ")

#Ordering Loop used for code
while True:
    # Check if we are not redirected to custom
    if redirected_to_custom == False:
        # Ask customer to input what kind of burger they want
        burger_choice = input("\nWould you like standard burger (S) or customized burger (C), enter No(N) to stop: ").lower()
        # Validating the burgers to make sure no other actions are taking place.
        while burger_choice != 'n' and burger_choice != 'c' and burger_choice != 's':
            burger_choice = input("\nPlease re-enter your choice. Would you like standard burger (S) or customized burger (C), enter No(N) to stop: ").lower()
    else:
        redirected_to_custom = False

    if burger_choice == 'n':
        break

    if burger_choice == 'c' or redirected_to_custom:
        total_burgers_customized += 1
        toppings_input = input("\nPlease enter your toppings, [S]auce, [P]ickles, [T]omato, [O]nion, [L]ettuce, [C]heese: ").lower()

        #Counting the max number of times a letter can be counted in a string using the min function
        sauce = min(toppings_input.count('s'), 2)
        pickles = min(toppings_input.count('p'), 2)
        tomato = min(toppings_input.count('t'), 2)
        onion = min(toppings_input.count('o'), 2)
        lettuce = min(toppings_input.count('l'), 2)
        cheese = min(toppings_input.count('c'), 2)

        #Order Summary Displayed
        print(f"You have ordered a customized burger with {sauce} sauce (s), {pickles} pickle(s), {tomato} tomato(es), {onion} onion(s), {lettuce} lettuce(s), and {cheese} cheese(es).")
        toppings_count = sauce + pickles + tomato + onion + lettuce + cheese

        #Calculate total time for the customized burger
        total_toppings_time = (toppings_count * TOPPING_TIME) + BUN_TIME + (STATION_TRAVEL_TIME * 6)
        total_cheese_time = (MELTING_TIME*cheese) + STATION_TRAVEL_TIME
        total_time_with_cheese = max(total_toppings_time, total_cheese_time) + (cheese * TOPPING_TIME) + STATION_TRAVEL_TIME
        total_time_patty = BURGER_COOK_TIME + STATION_TRAVEL_TIME
        total_time_for_custom = max(total_time_patty, total_time_with_cheese) + TOPPING_TIME + STATION_TRAVEL_TIME

        #Calculate initial cost for customized burger
        cost = BASE_COST + ((toppings_count - sauce - cheese) * 0.33) + (cheese * CHEESE_COST)

        #Calculate cost with any additional fees if relevant
        if 7 <= toppings_count <= 10:
            cost += ADDITIONAL_FEE_7TO10
        elif 11 <= toppings_count <= 12:
            cost += ADDITIONAL_FEE_11TO12

        #Cost and Time updates for customized
        total_cost += cost
        total_time = total_time_for_custom
        master_total_time += total_time
        minutes = total_time // 60
        seconds = total_time % 60

        #Printing how long it takes burger to get ready as well as its cost
        print(f"This burger will be ready in {minutes} minutes and {seconds} seconds.")
        print(f"This burger will cost ${cost:.2f}")

    #Standard Burger Ordering Process
    if burger_choice == 's':
        # Checking Burger availability to see if loop can run
        if total_burgers_standard >= MAX_STANDARD_BURGERS:
            while True:
                burger_choice = input("\nNo standard burgers available, please select customized burger (C), or enter No(N) to stop: ").lower()
                if burger_choice == 'n':
                    break
                elif burger_choice == 'c':
                    redirected_to_custom = True  # Set the flag when redirected
                    break
        if burger_choice == 'n':
            break
        if redirected_to_custom:
            continue  # Skip to the next iteration of the loop, which will handle the custom order due to the flag

        #Creating table for standard burgers showing burger amount, cost, and waiting time.
        remaining_burgers = MAX_STANDARD_BURGERS - total_burgers_standard
        print(f"\nYou can purchase 1 - {remaining_burgers} standard burgers, see the following for the cost and waiting time:")
        print(f'{"Burger Amount":<16} {"Cost":<17} {"Waiting Time":<15}')
        for i in range(1, remaining_burgers + 1):
            print(f'{i:<15} ${i * BURGER_PRICE:<10.2f} {(i * ADDITIONAL_TIME) // 60} minutes and {(i * ADDITIONAL_TIME) % 60} seconds')

        #Asking user for how many burgers they want and seeing if this is possible
        num_burgers = int(input("\nHow many standard burgers would you like to buy? "))
        if num_burgers > remaining_burgers:
            print(f"\nOnly {remaining_burgers} standard burger(s) can be ordered. Adjusting your order to {remaining_burgers}.")
            num_burgers = remaining_burgers

        #Cost and Time updates for Standard
        total_burgers_standard += num_burgers
        order_cost = num_burgers * BURGER_PRICE
        order_time = num_burgers * ADDITIONAL_TIME
        total_cost += order_cost
        master_total_time += order_time
        minutes = order_time // 60
        seconds = order_time % 60

        #Printing how many burgers ordered, how long they will take in minutes and seconds, and their cost
        print(f"\n{customer_name}, you ordered {num_burgers} standard burger(s) this time, the total standard burger(s) you ordered is {total_burgers_standard}.")
        print(f"{num_burgers} standard burgers will be ready in {minutes} minutes and {seconds} seconds.")
        print(f"The cost for {num_burgers} standard burger(s) is ${order_cost:.2f}")

#Ending outside the loop, showing the customer name, the overall amount of burgers ordered, the amount of time in minutes and seconds, and the total cost
print(f"\nThank you, {customer_name}, for shopping with us!")
minutes = master_total_time // 60
seconds = master_total_time % 60
print(f"This order for {total_burgers_standard + total_burgers_customized} burger(s) will be ready in {minutes} minutes and {seconds} seconds.")
print(f"The cost is ${total_cost:.2f}")