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

'''
seq = {'finance', 'accounting', 'economics'}
#initializing with None
dict1 = dict.fromkeys(seq)
print(f"The dictionary with None values: {dict1}")
#using fromkeys() to convert sequence to dict initializing with 1
dict2 = dict.fromkeys(seq, 1)
print(f"The newly created dictionary with 1 as value: {dict2}")
'''
'''
dict1 = {1: "finance", 2: "accounting", 3: "economics"}
print(f"The original disctionary is {dict1}")
dict2 = {4: "marketing"}
dict1.update(dict2)
print(f"The updates dictionary is {dict1}")
'''
'''
dict1 = {x: x * x for x in range(1,11)}
print(f"The dictionary is {dict1}")

dict2 = {x: x * x for x in range(1,11) if x * x % 2 == 1}
print(f"The new dictionary is {dict2}")
'''

'''
keys = [1,2,3,4]
values = ['finance', 'marketing', 'business', 'management']
#but this line shows dict comprehension here
print(list(zip(keys, values)))
dict1 = {k: v for (k, v) in zip(keys, values)}
print(f"The dictionary is {dict1}")
'''
'''
dict1 = {1: 10, 2: 20}
dict1.update({3: 30, 4: 40, 5: 50, 6: 60})
print(dict1)
'''
'''
dictHotel = {"New York": [185, 174, 190, 200], "Boston": [175, 1150, 185, 300], "Chicago": [18, 174, 1900, 200], "Los Angelos": [104, 15, 190, 200]}
print(f"The dictionary is {dictHotel}")

dictHotel["Dallas"] = [125, 250, 350, 200]
print(f"The dictionary is {dictHotel}\n")

priceList = []
for h in dictHotel:
    price = max(dictHotel[h])
    priceList.append(price)
    print(f"The most expensive hotel in {h} costs ${price:.2f}")

print(priceList)
hotel = []
for key in dictHotel:
    hotel.append(key)

print(hotel)
maxPrice = max(priceList)
value = priceList.index(maxPrice)
hotelName = hotel[value]

'''
'''
dict1 = {"course1": {"name": "CS150", "prof":"Smith"},
         "course2": {"name": "CS230", "prof": "Jones"},
         "course3": {"name": "CS100", "prof": "Samuels"}}
print(f"The dictionary is {dict1}/n")

for course in dict1:
    print(dict1[course])
    name = dict1[course]["name"]
    prof = dict1[course]["prof"]
    print(f"The professor for {name} is {prof}")

for course in dict1:
    if dict1[course]["name"] == "CS230":
        name = dict1[course]["name"]
        prof = dict1[course]["prof"]
        print(f"The professor for {name} is {prof}")

'''

restDict = [
    {"name": "Dunkin", "location": "Dedham, MA"},
{"name": "Red Fox", "location": "Jackson, NH"},
{"name": "Horsefeathers", "location": "North Conway, NH"},
{"name": "The Salty Pig", "location": "Boston, MA"}]

print(f"The dictionary is {restDict}\n")

print("restDict and their locations")
for c in restDict:
    print(f"{c["name"]}: {c["location"]}")

restDict[1]["location"] = "Kendall Square, Cambridge, MA"
print(f"\nRestaurants and their new locations")
for c in restDict:
    print(f"{c['name']}: {c['location']}")

for c in restDict:
    c["fee"] = 50.00
print("\nRestaurant and their new feed")
for c in restDict
    print(f"{c['name']}: {c['location']}")








