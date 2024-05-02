"""
Class: CS230--Section 3
Name: Vrishab Bharti
Description: AI Extra Credit
I pledge that I have completed the programming assignment
independently.
I have not copied the code from a student or any source.
I have not given my code to any student. 
"""
# Constants
BIKE_MODELS = {
    'M': {'name': 'Mountain Bike', 'price': 1550.00},
    'H': {'name': 'Hybrid Bike', 'price': 1150.00},
    'R': {'name': 'Road Bike', 'price': 1000.00}
}

FRAME_MATERIAL_OPTIONS = {
    'A': {'name': 'Aluminum', 'price': 200.00},
    'C': {'name': 'Carbon Fiber', 'price': 750.00},
    'S': {'name': 'Steel', 'price': 350.00},
    'M': {'name': 'Aluminum/Carbon Mix', 'price': 800.00}
}

FRAME_SIZE_OPTIONS = {
    'S': {'name': 'Small', 'price': 1000.00},
    'M': {'name': 'Medium', 'price': 1500.00},
    'L': {'name': 'Large', 'price': 2000.00}
}

HANDLEBAR_OPTIONS = {
    'F': {'name': 'Flat', 'price': 0.00},
    'R': {'name': 'Riser', 'price': 0.00},
    'D': {'name': 'Drop', 'price': 50.00}
}


# Function to get user input
def get_user_input(message, options):
    while True:
        choice = input(message).upper()
        if choice in options:
            return choice


# Function to calculate total price
def calculate_total_price(bike_model, frame_size, frame_material, handlebars):
    bike_price = BIKE_MODELS[bike_model]['price']
    frame_size_price = FRAME_SIZE_OPTIONS[frame_size]['price']
    frame_material_price = FRAME_MATERIAL_OPTIONS[frame_material]['price']
    handlebars_price = HANDLEBAR_OPTIONS[handlebars]['price']
    total_price = bike_price + frame_size_price + frame_material_price + handlebars_price
    return total_price


# Function to display bike configuration
def display_bike_configuration(bike_model, frame_size, frame_material, handlebars, total_price):
    print("****************************************************")
    print(f"    {BIKE_MODELS[bike_model]['name']} Configuration and Price:")
    print(f"Type of Bike:     {BIKE_MODELS[bike_model]['name']}             ${BIKE_MODELS[bike_model]['price']:.2f}")
    print(
        f"Bike Size:        {FRAME_SIZE_OPTIONS[frame_size]['name']}                     ${FRAME_SIZE_OPTIONS[frame_size]['price']:.2f}")
    print(
        f"Frame Material:   {FRAME_MATERIAL_OPTIONS[frame_material]['name']}                  ${FRAME_MATERIAL_OPTIONS[frame_material]['price']:.2f}")
    print(
        f"Handlebars:       {HANDLEBAR_OPTIONS[handlebars]['name']} Handlebars           ${HANDLEBAR_OPTIONS[handlebars]['price']:.2f}")
    print("=====================================================")
    print(f"Total Price:                                 ${total_price:.2f}")


# Main function
def main():
    print("Build a Bike")
    surface_choice = get_user_input(
        "What kind of biking do you do?\nA - Dirt road and trails\nB - Pavement and natural surfaces\nC - Paved roads and bike paths\nEnter your choice: ",
        ['A', 'B', 'C'])

    if surface_choice == 'A':
        bike_model = 'M'  # Mountain Bike
    elif surface_choice == 'B':
        bike_model = 'H'  # Hybrid Bike
    else:
        bike_model = 'R'  # Road Bike

    print(f"We recommend a {BIKE_MODELS[bike_model]['name']}.")

    frame_size = get_user_input(f"Your bike is available in size [S]mall, [M]edium, or [L]arge.\nEnter your choice: ",
                                ['S', 'M', 'L'])

    if bike_model == 'M':
        frame_material = get_user_input(
            "You can choose [A]luminum, [C]arbon Fiber, or Aluminum/Carbon [M]ix.\nEnter your choice: ",
            ['A', 'C', 'M'])
        handlebars = get_user_input("You can choose [F]lat or [R]iser Handlebars.\nEnter your choice: ", ['F', 'R'])
    elif bike_model == 'H':
        frame_material = 'A'  # Hybrid bikes come only in Aluminum frame
        handlebars = get_user_input("You can choose [R]iser Handlebars.\nEnter your choice: ", ['R'])
    else:
        frame_material = get_user_input("You can choose [A]luminum, [C]arbon Fiber, or [S]teel.\nEnter your choice: ",
                                        ['A', 'C', 'S'])
        handlebars = get_user_input("You can choose [D]rop or [R]iser Handlebars.\nEnter your choice: ", ['D', 'R'])

    product_code = bike_model + frame_size + frame_material + handlebars
    total_price = calculate_total_price(bike_model, frame_size, frame_material, handlebars)

    display_bike_configuration(bike_model, frame_size, frame_material, handlebars, total_price)


# Entry point of the program
if __name__ == "__main__":
    main()
