"""
Class: CS230--Section 3
Name: Vrishab Bharti
Description: Extra Credit Assignment (AI vs Personal code). This is Personal
I pledge that I have completed the programming assignment
independently.
I have not copied the code from a student or any source.
I have not given my code to any student. 
"""

#Menu
MENU = """
Build a Bike
What kind of biking do you do?  
        A - Dirt road and trails
        B - Pavement and natural surfaces
        C - Paved roads and bike paths
"""

#Dictionary displaying all keys and values
def display_configuration_and_price(bike, size, material, handlebar):
    prices_dict = {
        'Mountain Bike': 1550, 'Hybrid Bike': 1150, 'Road Bike': 1000,
        'Small': 1000, 'Medium': 1500, 'Large': 2000,
        'Aluminum': 200, 'Carbon Fiber': 750, 'Steel': 350, 'Aluminum/Carbon Mix': 800,
        'Flat': 0, 'Riser': 0, 'Drop': 50
    }

#This was done if the handlebar was riser and equal to Mountain Bike or Road Bike, as in both of these the "Riser" is valued differently then what is in the prices_dict.
    if handlebar == 'Riser':
        if bike == 'Mountain Bike':
            prices_dict['Riser'] = 50
        elif bike == 'Road Bike':
            prices_dict['Riser'] = 75

#This looks at the total sum of the keys in bike, size, material, and handlebar as well as sets the product code
    total_price = sum(prices_dict[key] for key in [bike, size, material, handlebar])
    product_code = f"{size[0]}{bike[0]}{material[0]}{handlebar[0]}"

#Prints the table
    print("\n" + "*" * 53)
    print(f"     {bike} {product_code} Configuration and Price:     ")
    print(f"Type of Bike:     {bike:<25} ${prices_dict[bike]:>8,.2f}")
    print(f"Bike Size:        {size:<25} ${prices_dict[size]:>8,.2f}")
    print(f"Frame Material:   {material:<25} ${prices_dict[material]:>8,.2f}")
    print(f"Handlebars:       {handlebar:<25} ${prices_dict[handlebar]:>8,.2f}")
    print("=" * 53)
    print(f"Total Price:                                ${total_price:>8,.2f}")

#Looks into what the dictionary would consist of for materials and handlebars for Hybrid Bike and Road Bike and Mountain Bike
def configure_bike(bike_type):
    materials_dict = {'Hybrid Bike': 'Aluminum', 'Road Bike': '[A]luminum, [C]arbon Fiber, [S]teel',
                 'Mountain Bike': '[A]luminum, [C]arbon Fiber, Aluminum/Carbon [M]ix'}
    handlebars_dict = {'Hybrid Bike': 'Riser', 'Road Bike': '[D]rop, [R]iser', 'Mountain Bike': '[F]lat, [R]iser'}

#Prints the availability using is not equal to operators if the bike type is not Hybrid
#Also presents the bike availability options
    print("Your bike is available in size [S]mall, [M]edium, or [L]arge.")
    if bike_type != 'Hybrid Bike':
        print("You can choose ", materials_dict[bike_type])
        print("You can choose ", handlebars_dict[bike_type])

#Asks to the choices from the options presented, and converts it to upper no matter what type is entered
    user_input = input("Enter your choice(s): ").upper()
    size = {'S': 'Small', 'M': 'Medium', 'L': 'Large'}[user_input[0]]

#This is what the material and haldebar is automatically eyal to for the hybrid bike as there is only one option for both
    if bike_type == 'Hybrid Bike':
        materials_dict = 'Aluminum'
        handlebars_dict = 'Riser'
    else:
        materials_dict = {'A': 'Aluminum', 'C': 'Carbon Fiber', 'M': 'Aluminum/Carbon Mix', 'S': 'Steel'}[user_input[1]]
        handlebars_dict = {'F': 'Flat', 'R': 'Riser', 'D': 'Drop'}[user_input[2]]

    display_configuration_and_price(bike_type, size, materials_dict, handlebars_dict)


def main():
    print(MENU)
    option = input("Enter your choice: ").upper()
    bike_types = {
        'A': 'Mountain Bike',
        'B': 'Hybrid Bike',
        'C': 'Road Bike'
    }
# Gives 3 different recommendations based on what type of (A, B, or C) the user picks
    if option == 'A':
        print("We recommend a Mountain Bike.")
    elif option == 'B':
        print("We recommend a Hybrid Bike.")
    elif option == 'C':
        print("We recommend a Road Bike.")
    configure_bike(bike_types[option])

if __name__ == "__main__":
    main()

