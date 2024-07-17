# Bar Graph Example
import matplotlib.pyplot as plt

# Path to the data file
file_path = 'C:/Users/Byhri/OneDrive/Desktop/Intro to Python SU24/homework9/last_ten_year_net_profit.txt'

# Reading data from the file
years = []
profits = []

with open(file_path, 'r') as file:
    next(file)  # Skip the header
    for line in file:
        year, profit = line.strip().split(';')
        years.append(int(year))
        profits.append(int(profit.replace('$', '').replace(',', '')))

# Creating the bar graph
plt.figure(figsize=(10, 7))
plt.bar(years, profits, color='skyblue')
plt.xlabel('Year')
plt.ylabel('Net Profit')
plt.title('Company’s Profit Over the Past Ten Years')
plt.show()
