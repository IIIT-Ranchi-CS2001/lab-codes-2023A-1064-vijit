import numpy as np
import pandas as pd

file_path = "D:\\Downloads\\AQI_Data.csv"
data = pd.read_csv(file_path)

df = pd.DataFrame(data)

# Load the dataset using Pandas and perform the following:

# a) Display the first 5 rows
print("First 5 rows of the dataset: ")
print(df.head(5))
print()

# b) Display the last 6 rows
print("Last 6 rows of the dataset: ")
print(df.tail(6))
print()
# c) Show the summary statistics of the dataframe
print("The summary statistics for all numeric columns: ")
print(df.describe())
print()
# d) Use NumPy to show the mean of AQI, PM2.5, and PM10 values for each city 
# Ensure the column names match the CSV file (adjust the names if necessary)


# Calculate the mean of AQI, PM2.5, and PM10 for each city
columns_to_mean = ['AQI', 'PM2.5', 'PM10']
mean_by_city = df.groupby('City')[columns_to_mean].agg(np.mean)

# Display the result
print("Mean values of AQI, PM2.5, and PM10 for each city:")
print(mean_by_city)
print()

#4 Group the data by city and calculate the following for each city: 
# a. Average AQI
# b. Maximum PM 10 level
# Save this grouped data inta a new csv file named Citywise_AQI.csv

grouped_stats = df.groupby('City').agg({
    'AQI': 'mean',        # Average AQI
    'PM10': 'max'         # Maximum PM10 level
}).rename(columns={
    'AQI': 'Average AQI',
    'PM10': 'Maximum PM10'
})

# Save the grouped data to a new CSV file
output_file_path = "D:\\Downloads\\Citywise_AQI.csv"
grouped_stats.to_csv(output_file_path)

# Display the grouped statistics
print("Grouped statistics for each city average AQI and max PM10:")
print(grouped_stats)
print()
print(f"The data has been saved to: {output_file_path}")
print()