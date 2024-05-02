"""
Class: CS230--Section 3
Name: Vrishab Bharti
Description:

Exercise #3:

See attached files: autos.csv and autos_start.py

The file autos.csv is a comma separated file containing basic car information from automobile manufacturers:

Index
Company
Body-style
Wheel-base
Length,
Engine-type
Num-of-cylinders
Horsepower
Average-mileage
Price
Here are the first few lines:

index,company,body-style,wheel-base,length,engine-type,num-of-cylinders,horsepower,average-mileage,price
0,Alfa-Romero,convertible,88.6,168.8,dohc,four,111,21,13495
1,Alfa-Romero,convertible,88.6,168.8,dohc,four,111,21,16500
2,Alfa-Romero,hatchback,94.5,171.2,ohcv,six,154,19,16500
3,Audi,sedan,99.8,176.6,ohc,four,102,24,13950
4,Audi,sedan,99.4,176.6,ohc,five,115,18,17450
5,Audi,sedan,99.8,177.3,ohc,five,110,19,15250
(the rest of the data is omitted)

In this program, you will read the in the CSV file and store its values in a Pandas DataFrame. Use features of the DataFrame to calculate the number of cars manufactured by each company and graph that, calculate the highest price car of each company, find the average mileage of each car company, and ask the user to enter a company name and display all the information about that company.

Start with the autos_start.py file. Make all your changes to this file.

Read the data into a DataFrame as part of the main() function. (2 points)
Write the priceCars function to calculate the number of cars manufactured by each company and crate a bar chart of that data. Update the parameters to this function as needed. (6 points)
Write the calculateSales function to calculate the highest price car of each company.  Update the parameters to this function as needed. (4 points)
Write the averageCars function to calculate the average mileage of each car company. Update the parameters to this function as needed. (4 points)
Write the filterCars function to display all the information about the company which the user inputs. Update the parameters to this function as needed. (4 points)
Sample output is as follows (not all data is shown and graph is not shown):

I pledge that I have completed the programming assignment
independently.
I have not copied the code from a student or any source.
I have not given my code to any student. 
"""
import pandas as pd
import matplotlib.pyplot as plt

FILENAME = "autos.csv"

def read_data():
    return pd.read_csv(FILENAME)

def countCars(df):
    car_counts = df['company'].value_counts()
    fig, ax1 = plt.subplots(figsize=(15, 10))

    positions = range(len(car_counts))
    labels = car_counts.index.tolist()

    ax1.xaxis.set_ticks(positions)
    ax1.xaxis.set_ticklabels(labels, rotation=45, ha='right')
    ax1.set_xlabel('Manufacturers')
    ax1.set_ylabel('Number of Cars')
    ax1.set_title('Number of Cars Manufactured by Each Company')
    ax1.bar(positions, car_counts.values, color='b')

    plt.show()
    return car_counts

def priceCars(df):
    return df.loc[df.groupby('company')['price'].idxmax()][['company', 'price']]

def averageCars(df):
    return df.groupby('company')['average-mileage'].mean()

def filterCars(df, company):
    return df[df['company'].str.lower() == company.lower()]

def main():
    df = read_data()
    run = True
    while run:
        choice = int(input("""
        =============Car Company Data=============

        1 - Number of Cars from Each and Bar Chart
        2 - Highest Price Car of Each Company 
        3 - Average Mileage of Each Car Company
        4 - Filter by Company Name
        5 - Quit 
        Enter choice: """))
        if choice == 1:
            car_counts = countCars(df)
            print(car_counts)
            plt.show()

        elif choice == 2:
            highest_price = priceCars(df)
            print(highest_price)

        elif choice == 3:
            average_mileage = averageCars(df)
            print(average_mileage)

        elif choice == 4:
            comp = input("Show all cars from: ")
            dfResults = filterCars(df, comp)
            print(dfResults)

        elif choice == 5:
            run = False

main()
