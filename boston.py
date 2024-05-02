"""
Class: CS230--Section 3
Name: Vrishab Bharti
Description: Homework Assignment 4 - Boston Attractions
I pledge that I have completed the programming assignment
independently.
I have not copied the code from a student or any source.
I have not given my code to any student.
"""

'''
Name: Vrishab Bharti
Date: 04/16/2024
Description: Use dictionaries and lists to manage data and show locations on the map
'''

import os
import webbrowser
import folium
import csv

columns = ['Short Name', 'Name', 'Category', 'URL', 'Lat', 'Lon', 'Color']
MENU = """
=====================================================================
1. Find an attraction by name       2. Find attractions by category
3. Add an attraction                4. Edit an attraction
5. Delete an attraction             6. Display all attractions
7. Quit
=====================================================================
"""
attractions = []

#Opens file bonston.csv in read mode and loads the data to the global attractions list. uses def function, Dictreader which identifies the keys of the dictionaries. Reading row by row in the reader
def openfile():
    '''
    Read the data from the data file
    Add the dictionaries to the list (attractions)
    '''
    global attractions
    with open('boston.csv', mode='r') as file:
        reader = csv.DictReader(file)
        attractions = [row for row in reader]

#Looks into using a for and if loop, uses def function, shortname for the list of dictionaries
def findbyname():
    '''Find an attraction by its short name'''
    name = entername()
    for attraction in attractions:
        if attraction['Short Name'] == name:
            print("Attraction details:")
            for key, value in attraction.items():
                print(f"{key:<12}: {value}")
            return
    print("Attraction not found.")

#User is asked to enter what category of attraction they are looking for, list of attractions is printed with their name and URL.
def findbycat():
    '''Find attractions by category'''
    categories = {'e': 'events', 's': 'shopping', 't': 'tourism', 'u': 'university'}
    prompt = "Which type of attractions do you like to visit? [E]vents, [S]hopping, [T]tourism, or [U]university: "

    while True:
        category_key = input(prompt).lower()
        if category_key in categories:
            category = categories[category_key]
            found = False
            print(f"\n{category.upper()} attractions in Greater Boston:")
            print(f"{'Name':<80}URL")
            for attraction in attractions:
                if attraction['Category'].lower() == category:
                    print(f"{attraction['Name']:<80}{attraction['URL']}")
                    found = True
            if not found:
                print("No attractions found for this category.")
            break
        else:
            print("Invalid Input! Please try again.")

#I made it so that when option 6 is picked, the showonmap also plays. This makes most sense to me as from a user pespective.
#lists all attractions sorter by Name in ascending order and they are formatted
def allattractions():
    '''List and display all attractions'''
    if attractions:
        sorted_attractions = sorted(attractions, key=lambda x: x['Name'])
        showonmap(sorted_attractions)
        print(f"{'Name':<40}{'Category':<30}{'URL':<80}{'Color'}")
        for attraction in sorted_attractions:
            print(f"{attraction['Name']:<40}{attraction['Category']:<30}{attraction['URL']:<80}{attraction['Color']}")

#asks user to enter information for new attraction. Splits the information entered, constructs a dictionary for this new information, and appends it into the global attraction list
def addattraction():
    '''Add a new attraction'''
    global attractions
    name = entername(required_exists=False)
    data = input("Please enter the new attraction info (Name, Category, URL, Lat, Lon, Color): \n")
    details = data.split(',')
    new_attraction = {
        'Short Name': name,
        'Name': details[0],
        'Category': details[1],
        'URL': details[2],
        'Lat': details[3],
        'Lon': details[4],
        'Color': details[5]
    }
    attractions.append(new_attraction)
    print(f"You have added a new attraction for {details[0]}")

#Asks the user to pick what color they want the new color to be and changes the color in the map. Gives three options for colors. Uses Boolean, if-else, if-not.
def editattraction():
    '''Change the marker color of an attraction'''
    name = entername()
    found = False
    for attraction in attractions:
        if attraction['Short Name'].lower() == name.lower():
            found = True
            while True:
                new_color = input("Please enter the new color ([g]reen, [b]lue, [o]range), press Enter to keep the old color: ").lower()
                color_map = {'g': 'green', 'b': 'blue', 'o': 'orange'}
                if new_color == '' or new_color in color_map:
                    if new_color:
                        attraction['Color'] = color_map[new_color]
                        print(f"You have successfully changed the color of the icon to {color_map[new_color]}.")
                    else:
                        print("No changes made to the color.")
                    return
                else:
                    print("Invalid input! Please try again.")
    if not found:
        print(f"Attraction {name} is not found. Please try again.")

#Deletes the attractions in the global attraction list.
def deleteattraction():
    '''Delete an attraction'''
    global attractions
    name = entername()
    initial_count = len(attractions)
    attractions = [attraction for attraction in attractions if attraction['Short Name'] != name]
    if len(attractions) < initial_count:
        print("Attraction deleted successfully.")
    else:
        print("Attraction not found.")

#Used as saving any changes made to the data file or exiting the program
def quit():
    '''Quit the program and write the info back to the data file'''
    with open('boston.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        writer.writerows(attractions)
    print("Have a nice day!")
    exit()

#Used to show the attractions on the map. Used the demo_folium.py file for this
def showonmap(placelist):
    icon_names = {
        "university": "graduation-cap",
        "tourism": "camera",
        "shopping": "shopping-cart",
        "events": "flag"
    }

    center = [42.36165764, -71.08567345]  # The [lat, lon] of the center of Boston
    bostonmap = folium.Map(location=center, zoom_start=12)

    for place in placelist:
        lat = float(place['Lat'])
        lon = float(place['Lon'])
        category = place['Category'].lower()
        icon_type = icon_names.get(category, "flag")
        icon = folium.Icon(icon=icon_type, prefix="fa", color=place.get('Color', 'blue'))

        folium.Marker(
            location=[lat, lon],
            popup=f'<a href="{place["URL"]}" target="_blank">{place["Name"]}</a>',
            tooltip=place["Name"],
            icon=icon
        ).add_to(bostonmap)

    filePath = os.path.join(os.getcwd(), "bostonmap.html")
    bostonmap.save(filePath)
    webbrowser.open('file://' + os.path.realpath(filePath))

#This one was tricky, as i wanted to challenge myself and simplify the code to the point where "new" would only be printed in one of the codes since its only mentioned when you addattraction. This code also looks at two scenarioes, one wehre the attraction does not exist when you look for it in the list and another when the attraction already exists

def entername(required_exists=True):
    '''Process user input for the short name of an attraction'''
    while True:
        action_text = "new " if not required_exists else ""
        name = input(f"Please enter the short name of the {action_text}attraction: ").lower()
        exists = any(attraction['Short Name'].lower() == name for attraction in attractions)
        if required_exists and not exists:
            print("Attraction not found. Please try again.")
        elif not required_exists and exists:
            print("Attraction already exists. Please try again.")
        else:
            return name

#Given in the boston_starter.py file
def main():
    openfile()

    while True:
        print(MENU)
        option = input("Please select an option: ")
        if option not in '1234567':
            print("Invalid input! An option must be a number between 1 and 7.")
            continue

        option = int(option)
        if option == 1:
            findbyname()
        elif option == 2:
            findbycat()
        elif option == 3:
            addattraction()
        elif option == 4:
            editattraction()
        elif option == 5:
            deleteattraction()
        elif option == 6:
            allattractions()
        elif option == 7:
            quit()

main()