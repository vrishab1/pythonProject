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

import pandas as pd
'''
data = {'apples':[150, 175, 200, 125],
        'pears':[250, 135, 325, 645],
        'peaches and plums': [175, 150, 160, 200]}

df = pd.DataFrame(data, index=['Store 1', 'Store 2', 'Store 3', 'Store 4'])
print(f"The DataFrame is \n{df}")

bananas = [275, 450, 150, 175]
df['bananas'] = bananas

#popped_column = df.pop('peaches and plums')
#df = df.rename(columns={'peaches and plums' : 'plums'})
print(f"The Original Dataframe is \n{df}")
print(f"\nThe Bananas Dataframe is \n{df}")
'''
cars = {'Model': ['Ford Focus', 'Honda Civic', 'Toyota Corolla', 'Volkswagen Golf', 'BMW X5'],
        'Price': [37.8, 35.7, 50.6, 35.5, 45.5],
        'Tank': [13.9, 12.4, 13.2, 13.2, 21.9]}
df = pd.DataFrame(cars, columns = ['Model', 'Price', 'MPG', 'Tanks'])

print(f"The Original DataFrame is\n{df}")
print(f"\nThe sum of the price column is\n{df['Price'].sum()}")
print(f"\nThe sum of the price column is\n{df[['Price', 'MPG']].sum()}")