"""
Class: CS230--Section 3
Name: Vrishab Bharti
Description:
Exercise 1:
Create a DataFrame from the following dictionary:

data = {'apples': [150, 175, 200, 125],
'pears': [250, 135, 325, 645],
'bananas': [250, 135, 325, 645], }

Then do the following:

increase the inventory of the pears by 25 percent
add a column which displays the average of the fruit inventory in each store, rounded to two decimal places
Sample output is shown below:

The original DataFrame
         apples  pears  bananas
Store 1     150    250      250
Store 2     175    135      135
Store 3     200    325      325
Store 4     125    645      645
A 25% increase in pears
         apples   pears  bananas
Store 1     150  312.50      250
Store 2     175  168.75      135
Store 3     200  406.25      325
Store 4     125  806.25      645
The average of all fruits
         apples   pears  bananas  average
Store 1     150  312.50      250   237.50
Store 2     175  168.75      135   159.58
Store 3     200  406.25      325   310.42
Store 4     125  806.25      645   525.42

Exercise #2:

Create a DataFrame with the following data and assign it to a DataFrame called cities:

cities = {"name": ["London", "Berlin", "Madrid", "Rome", "Paris", "Vienna", "Bucharest", "Hamburg", "Budapest", "Warsaw", "Barcelona", "Munich", "Milan"], "population": [8615246, 3562166, 3165235, 2874038, 2273305, 1805681, 1803425, 1760433, 1754000, 1740119, 1602386, 1493900, 1350680], "country": ["England", "Germany", "Spain", "Italy", "France", "Austria", "Romania", "Germany", "Hungary", "Poland", "Spain", "Germany", "Italy"]}
Then do the following:

Rename the columns to Name, Population, Country.
Set the index to Country
Find all the cities in Germany and display those cities
Find all the cities whose population is greater than 300,000 and display those cities
Then sort those cities in ascending order by population
Add a column called Area to the original DataFrame (with the columns renamed but not setting Country as the index) using these values
area = [1572, 891.85, 605.77, 1285, 105.4, 414.6, 228, 755, 525.2, 517, 101.9, 310.4, 181.8]
Sort the columns by Area.
Using this DataFrame, find those whose area is greater than 500 and located in Germany.

I pledge that I have completed the programming assignment
independently.
I have not copied the code from a student or any source.
I have not given my code to any student. 
"""


print("\nExercise 1\n")
import pandas as pd

data_dict = {'apples': [150, 175, 200, 125],
'pears': [250, 135, 325, 645],
'bananas': [250, 135, 325, 645], }

df = pd.DataFrame(data_dict, index = ['Store 1', 'Store 2', 'Store 3', 'Store 4'])
print(f"\nThe original DataFrame\n{df}")
df['pears'] *= 1.25
print(f"\nA 25% increase in pears\n{df}")
df['average'] = df.mean(axis=1).round(2)
print(f"\nThe average of all fruits\n{df}")

print("\nExercise 2\n")

import pandas as pd

cities_dict = {"name": ["London", "Berlin", "Madrid", "Rome", "Paris", "Vienna", "Bucharest", "Hamburg", "Budapest", "Warsaw", "Barcelona", "Munich", "Milan"], "population": [8615246, 3562166, 3165235, 2874038, 2273305, 1805681, 1803425, 1760433, 1754000, 1740119, 1602386, 1493900, 1350680], "country": ["England", "Germany", "Spain", "Italy", "France", "Austria", "Romania", "Germany", "Hungary", "Poland", "Spain", "Germany", "Italy"]}

df = pd.DataFrame(cities_dict)
df = df.rename(columns={'name':'Name', 'population':'Population', 'country':'Country'})
df.set_index("Country", inplace=True)
df2 = df.loc["Germany"]
print(f"\nAll the cities in Germany\n{df2}")
df.reset_index(inplace=True)
df3 = df[df["Population"] > 300000].sort_values("Population")
print(f"\nAll the cities whose population is greater than 300,000 and sorted in ascending order by population\n{df3}")
Area_dict = [1572, 891.85, 605.77, 1285, 105.4, 414.6, 228, 755, 525.2, 517, 101.9, 310.4, 181.8]
df = df.assign(Area=Area_dict).sort_values("Area")
df4 = df[(df["Area"] > 500) & (df["Country"] == "Germany")]
print(f"\nUsing this DataFrame, find those whose area is greater than 500 and located in Germany.\n{df4}")



