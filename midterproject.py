import pandas as pd     # Pandas is a library for data manipulation and analysis
import matplotlib.pyplot as plt  # Matplotlib is a plotting library

# Step 1: Reading CSV File
df = pd.read_csv('data.csv')
print(df)

# Step 2: Total Sale
vehicles_sold_per_year = df.groupby('Year')['Vehicles Sold'].sum()  # Group by Year and sum Vehicles Sold
with open('stats.txt', 'w') as f: # Open file in write mode
    f.write(vehicles_sold_per_year.to_string()) # Write to file

# Step 3: Bar Plot
total_sales_per_year = df.groupby('Year')['Sales'].sum() # Group by Year and sum Sales
total_sales_per_year.plot(kind='bar') # Plot bar chart
plt.title('Total Sales per Year (2012-2021)') # Set title
plt.xlabel('Year') # Set x label
plt.ylabel('Total Sales') # Set y label
plt.show() # Show plot

# Step 4: Sale Estimation
sales_2021 = df[(df['Year'] == 2021) & (df['Month'] <= 6)]['Sales'].sum() # Get total sales for first 6 months of 2021
sales_2022 = df[(df['Year'] == 2022) & (df['Month'] <= 6)]['Sales'].sum() # Get total sales for first 6 months of 2022
sgr = (sales_2022 - sales_2021) / sales_2021 # Calculate Sales Growth Rate
with open('stats.txt', 'a') as f: # Open file in append mode

    f.write(f'\nSales Growth Rate (first 6 months of 2022): {sgr:.2f}\n') # Write to file
estimated_sales = [] # Create empty list
for month in range(7, 13): # Loop through months 7 to 12

    sale_2021 = df[(df['Year'] == 2021) & (df['Month'] == month)]['Sales'].sum() # Get total sales for month in 2021
    estimated_sale_2022 = sale_2021 + sale_2021 * sgr # Calculate estimated sales for month in 2022
    estimated_sales.append(estimated_sale_2022) # Append to list
    
with open('stats.txt', 'a') as f: # Open file in append mode
    f.write('Estimated Sales for last six months of 2022:\n') # Write to file
    for month, estimated_sale in zip(range(7,13), estimated_sales): # Loop through months and estimated sales
        f.write(f'Month {month}: {estimated_sale:.2f}\n') # Write to file

# Step 5: Horizontal Bar Plot
plt.barh(range(7,13), estimated_sales) # Plot horizontal bar chart
plt.title('Estimated Sales for last six months of 2022') # Set title
plt.xlabel('Estimated Sales')   # Set x label
plt.ylabel('Month') # Set y label
plt.yticks(range(7,13)) # Set y ticks
plt.show()