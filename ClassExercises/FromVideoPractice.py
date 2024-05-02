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
EmployeeDict = {}  # This will store text file data

with open('sales.txt', 'r') as file:
    # data = (Get the data from file - a list of lines ex [line1, line2, ...])
    for i in range(1, len(data)):
        # line = (us the indexes to go through rows of data)
        EmployeeID = line[0]
        EmployeeName = line[1]
        Position = line[2]
        Department = line[3]
        # line[-1] = line[-1] (the last value still has \n, remove it)
        # Sales = (this should equal a list of all the quarter sale)
        EmployeeDict[EmployeeID] = [EmployeeName, Position, Department, Sales]
    file.close()

print(EmployeeDict)  # ex {'1': ['John Doe', 'Sales Associate', 'Sales', ['15000', '18000', '20000', '22000']],...}

"""TotalSales = 0.0  # This will be used later when calculating employee sales average
EmployeeSale = {}  # This will be used to calculate the top earners {saleTotal:name}
DepartmentSale = {}  # This will be used to keep track of departmental sales {department:totalSales}
print('\n')
print(f"{'Yearly Sales':^35s}")
print("="*35)
for EmployeeID in EmployeeDict:
    # Employee = (this should retrieve the employee info using the EmployeeID dict key from for loop)
    # EmployeeName = (get data from Employee)
    # Department = (get data from Employee)
    # SalesTotal = (use list comprehension to sum up the list of quarter sale)
    # TotalSales (this should keep a running total of SalesTotal)
    EmployeeSale[SalesTotal] = EmployeeName
    # if (this should test if a department is already in the Department Sale Dictionary)
        DepartmentSale[Department] += SalesTotal
    else:
        DepartmentSale[Department] = SalesTotal
    print(f"{EmployeeName:<22s}${SalesTotal:>12,.2f}")"""

"""print('\n')
print(f"{'Department Sales':^35s}")
print("="*35)
# Create a for loop going through the DepartmentSale Dict
    # get the data associated with Department
    print(f"{Name:<22s}${Sales:>12,.2f}")"""


# SortedSales = Sort the Sales dict based, make sure it is in descending order based on sales amount
NUMEMPLOYEEWITHBONUS = 5

"""def calculate_bonus(saleamount):
    pass
    AverageEmployeeSale = TotalSales / 10
    # bonus = (calculate difference from average, and get the 20% bonus from that)
    # return bonus uncomment


print("\n")
print(f"{'Employee Bonuses':^35s}")
print("="*35)
for SaleAmount in SortedSales[:NUMEMPLOYEEWITHBONUS]:
    # Name = (get the employee name)
    # Bonus = (call the calculate_bonus function)
    print(f"{Name:<22s}${Bonus:>12,.2f}")"""
