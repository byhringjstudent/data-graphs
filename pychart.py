# Pie Chart example
import matplotlib.pyplot as plt

# Path to the data file
file_path = 'C:/Users/Byhri/OneDrive/Desktop/Intro to Python SU24/ch9/employee_count_by_department.txt'

# Reading data from the file
departments = []
counts = []

with open(file_path, 'r') as file:
    next(file)  # Skip the header
    for line in file:
        department, count = line.strip().split(',')
        departments.append(department)
        counts.append(int(count))

# Creating the pie chart
plt.figure(figsize=(10, 7))
plt.pie(counts, labels=departments, autopct='%1.1f%%')
plt.title('Percentage of Employees in Each Department')
plt.show()
