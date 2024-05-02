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

import matplotlib.pyplot as plt

'''
yAxis = [5,10,15,20,25]
xAxis = [1,2,3,4,5]

plt.bar(xAxis, yAxis)
plt.show()

yAxis = [5,10,15,20,25]
xAxis = [1,2,3,4,5]
plt.bar(xAxis, yAxis, width=.5)
plt.show()
'''

'''
data = [230, 850, 720, 430, 520]
labels = ["Northeast", "South", "Mid-Atlantic", "Midwest", "West"]
plt.xticks(range(len(data)), labels)
plt.xlabel("Regions")
plt.ylabel("Amounts")
plt.title("Sales")
plt.barh(range(len(data)), data,color="maroon")
plt.show()
'''

'''
data = {"Northeast":230, "South":850, "Mid-Atlantic":720, "Midwest":430, "West":520}
days = list(data.keys())
values = list(data.values())
plt.xlabel("Regions")
plt.ylabel("Amounts")
plt.title("Sales")
plt.barh(range(len(data)), data,color="maroon")
plt.show()
'''
'''
data = [230, 850, 720, 430, 520]
data2 = [350, 450, 250, 520, 430]
labels = ["Northeast", "South", "Mid-Atlantic", "Midwest", "West"]
plt.xticks(range(len(data)), labels)
plt.xlabel("Regions")
plt.ylabel("Amounts")
plt.title("Sales")
plt.bar(range(len(data)), data,color="r")
plt.bar(range(len(data)), data2,color="b", bottom=data)
plt.show()
'''

'''
data1 = [23, 85, 72, 43, 52]
data2 = [42, 35, 21, 16, 9]
width = 0.4
t = list(range(len(data1)))
t1 = [x - (width/2) for x in t]
t2 = [x + (width/2) for x in t]
labels = ["Northeast", "South", "Mid-Atlantic", "Midwest", "West"]
plt.xticks(range(len(data1)), labels)
plt.xlabel("Regions")
plt.bar(t1, data1, color="#ff8000", width=width, label = "Quarter 1")
plt.bar(t2, data2, color="r", width=width, label = "Quarter 2")
plt.title("Numbers")
plt.legend(loc="best")
plt.show()
'''
'''
data1 = [5200, 5100, 4550, 5870, 4560]
data2 = [1200, 2100, 3550, 1870, 1560]
width = 0.4
t = list(range(len(data1)))
t1 = [x + (width/2) for x in t]
t2 = [x - (width/2) for x in t]
labels = ["Northeast", "South", "Mid-Atlantic", "Midwest", "West"]
plt.xticks(range(len(data1)), labels)
plt.xlabel("Regions")
plt.bar(t1, data1, color="b", width=width, label = "Quarter 1")
plt.bar(t2, data2, color="r", width=width, label = "Quarter 2")
plt.title("Numbers")
plt.legend(loc="best")
plt.show()
'''
'''
regions = ["Northeast", "South", "Mid-Atlantic", "Midwest", "West"]
sales = [230, 850, 720, 430, 520]
plt.pie(sales, labels=regions, autopct="%1.2f%%")
plt.title("Sales by Region")
plt.show()
'''
regions = ["Northeast", "South", "Mid-Atlantic", "Midwest", "West"]
sales = [230, 850, 720, 430, 520]
colors = ["gold", 'yellowgreen', "lightcoral", "lightskyblue", "aquamarine"]
plt.title('Sales by Region')
plt.pie(sales, explode=[0,0,0,.2,0], colors = colors, labels=regions, autopct="%1.2f%%")
plt.show()



