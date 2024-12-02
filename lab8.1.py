import numpy as np
import matplotlib.pyplot as plt

covid_data = np.array([
    [1500, 2000, 1800, 1200, 900],
    [1600, 2100, 1900, 1300, 950],
    [1700, 2200, 2000, 1400, 1000],
    [1650, 2150, 1950, 1350, 980],
    [1750, 2250, 2050, 1450, 1020],
    [1800, 2300, 2100, 1500, 1050],
    [1900, 2400, 2200, 1600, 1100]
])

countries = ["Country_A", "Country_B", "Country_C", "Country_D", "Country_E"]

# Basic Statistics
total_cases = np.sum(covid_data, axis=0)
highest_cases_country = countries[np.argmax(total_cases)]
print(f"Total cases by country: {total_cases}")
print(f"Country with the highest cases: {highest_cases_country}")

# Daily Analysis
daily_avg_cases = np.mean(covid_data, axis=1)
highest_cases_day = np.argmax(np.sum(covid_data, axis=1)) + 1
print(f"Average daily cases: {daily_avg_cases}")
print(f"Day with the highest total cases: Day {highest_cases_day}")

# Trends
percentage_changes = ((covid_data[-1] - covid_data[0]) / covid_data[0]) * 100
highest_increase_country = countries[np.argmax(percentage_changes)]
print(f"Percentage changes from Day 1 to Day 7: {percentage_changes}")
print(f"Country with the highest percentage increase: {highest_increase_country}")

# Data Transformation
normalized_data = (covid_data - np.min(covid_data, axis=0)) / (np.max(covid_data, axis=0) - np.min(covid_data, axis=0))
print("Normalized data:")
print(normalized_data)

# Visualization
days = np.arange(1, 8)
fig, ax = plt.subplots(figsize=(10, 6))

for i, country in enumerate(countries):
    ax.plot(days, covid_data[:, i], label=country)

ax.set_title("Daily COVID-19 Cases by Country")
ax.set_xlabel("Day")
ax.set_ylabel("Cases")
ax.legend()
ax.grid(True)

highest_cases_day_total = np.sum(covid_data, axis=1).max()
ax.annotate(
    f"Highest: Day {highest_cases_day}",
    xy=(highest_cases_day, highest_cases_day_total),
    xytext=(highest_cases_day - 1, highest_cases_day_total + 500),
    arrowprops=dict(facecolor='red', arrowstyle="->"),
    fontsize=10
)

plt.tight_layout()
plt.show()
