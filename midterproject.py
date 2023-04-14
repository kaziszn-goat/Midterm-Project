import csv
import matplotlib.pyplot as plt

# Step 1: Reading CSV File
with open('data.csv', 'r') as file: 
    reader = csv.reader(file) 
    for row in reader: 
        print(row) 

# Step 2: Total Sale
sales = {} 
with open('data.csv', 'r') as file: 
    reader = csv.DictReader(file) 
    for row in reader:          
        year = int(row['Year'])
        if 2012 <= year <= 2021:
            sales[year] = sales.get(year, 0) + int(row['Sales']) 
with open('stats.txt', 'w') as file:
    for year, total_sales in sales.items():
        file.write(f'{year}: {total_sales}\n')  

# Step 3: Bar Plot 
plt.bar(sales.keys(), sales.values())
plt.show()

# Step 4: Sale Estimation
sales_2021 = {}
sales_2022 = {}
with open('data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        year = int(row['Year'])
        month = int(row['Month'])
        if year == 2021 and month <= 6:
            sales_2021[month] = int(row['Sales'])
        elif year == 2022 and month <= 6:
            sales_2022[month] = int(row['Sales'])
total_sales_2021 = sum(sales_2021.values())
total_sales_2022 = sum(sales_2022.values())
sgr = (total_sales_2022 - total_sales_2021) / total_sales_2021
with open('stats.txt', 'a') as file:
    file.write(f'Sales Growth Rate: {sgr}\n')
    for month in range(7, 13):
        estimated_sale = sales_2021[month] + sales_2021[month] * sgr
        file.write(f'Estimated sale in month {month} of 2022: {estimated_sale}\n')

# Step 5: Horizontal Bar Plot
estimated_sales = []
for month in range(7, 13):
    estimated_sale = sales_2021[month] + sales_2021[month] * sgr
    estimated_sales.append(estimated_sale)
plt.barh(range(7, 13), estimated_sales)
plt.show()