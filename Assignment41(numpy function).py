#Suppose you have a dataset containing daily temperature readings for a city, and you want to identify days with extreme temperature conditions. Find days where the temperature either exceeded 35 degrees Celsius (hot day) or dropped below 5 degrees Celsius (cold day). Input: temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2])
import numpy as np

# Given temperatures
temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2])

# Boolean condition for hot days (temperature > 35)
hot_days = temperatures > 35

# Boolean condition for cold days (temperature < 5)
cold_days = temperatures < 5

# Combine the conditions to find extreme temperature days
extreme_days = hot_days | cold_days

# Indices of days with extreme temperature conditions
extreme_days_indices = np.where(extreme_days)[0]

print("Days with extreme temperatures:", extreme_days_indices)

#output
Days with extreme temperatures: [2 5 9]
