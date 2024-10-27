# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 21:50:49 2023

@author: anupi
"""

import FedEx1 as fe
import ParcelChief as pc
import re
import matplotlib.pyplot as plt
import numpy as np

print("Shipping to Pittsburgh")
destinationCity = "Pittsburgh"

valid_inputs = {'Mumbai', 'Bengaluru', 'Hyderabad'}
originCity = input("Enter origin city (Only shipping from Mumbai, Bengaluru and Hyderabad at the moment): ").title()

while originCity not in valid_inputs:
    print("Invalid input. Please enter Mumbai, Bengaluru or Hyderabad.")
    originCity = input("Enter origin city (Only shipping from Mumbai, Bengaluru and Hyderabad at the moment): ").title()


while True:
    weight = input("Enter weight of the parcel to be shipped (up to 500): ")

    try:
        weight = int(weight)
        if 0 < weight <= 500:
            break  # Exit the loop if the input is a valid integer within the range
        else:
            print("Invalid input. Please enter an integer up to 500.")
    except ValueError:
        print("Invalid input. Please enter an integer.")
try:
    print("Getting data for FedEx")
    fedex_delivery_days, fedex_delivery_prices, fedex_delivery_types = fe.fedex(originCity, destinationCity, weight)
except:
    print("Error while reading data from FedEx")

    fedex_delivery_days = []
    fedex_delivery_prices = []
    fedex_delivery_types = []
    
    
try:
    print("Getting data for Parcel Chief")
    parcelchief_delivery_days, parcelchief_delivery_prices, parcelchief_delivery_types = pc.parcelchief(weight)
except:
    print("Error while reading data from Parcel Chief")
    parcelchief_delivery_days = []
    parcelchief_delivery_prices = []
    parcelchief_delivery_types = []
    

print(fedex_delivery_days)
print(fedex_delivery_prices)
print(fedex_delivery_types)
print(parcelchief_delivery_days)
print(parcelchief_delivery_prices)
print(parcelchief_delivery_types)


fedex_delivery_prices_numeric = [float(re.sub(r'[^\d.]', '', price)) for price in fedex_delivery_prices]


delivery_days = fedex_delivery_days + parcelchief_delivery_days
delivery_prices = fedex_delivery_prices_numeric + parcelchief_delivery_prices
delivery_types = fedex_delivery_types + parcelchief_delivery_types

print(delivery_days)
print(delivery_prices)
print(delivery_types)

# Plotting delivery days
plt.figure(figsize=(10, 5))
plt.bar(delivery_types, delivery_days, color='skyblue')
plt.title('Delivery Days')
plt.xlabel('Delivery Type')
plt.ylabel('Delivery Days')
plt.xticks(rotation=45, ha='right')
plt.show()

# Plotting delivery prices
plt.figure(figsize=(10, 5))
plt.bar(delivery_types, delivery_prices, color='lightcoral')
plt.title('Delivery Prices')
plt.xlabel('Delivery Type')
plt.ylabel('Delivery Price (in ₹)')
plt.xticks(rotation=45, ha='right')
plt.show()


x = np.arange(len(delivery_types))

# Plotting all fields in a grouped bar chart
fig, ax1 = plt.subplots(figsize=(12, 6))

# Plotting delivery days
ax1.bar(x - 0.2, delivery_days, width=0.2, color='skyblue', label='Delivery Days')

# Plotting delivery prices on a secondary y-axis
ax2 = ax1.twinx()
ax2.bar(x, delivery_prices, width=0.2, color='lightcoral', label='Delivery Prices')

# Labeling the secondary y-axis
ax2.set_ylabel('Delivery Price (in ₹)', color='lightcoral')
ax2.tick_params(axis='y', labelcolor='lightcoral')

# Set x-axis ticks and labels
ax1.set_xticks(x)
ax1.set_xticklabels(delivery_types, rotation=45, ha='right')
ax2.set_xticks(x)
ax2.set_xticklabels(delivery_types, rotation=45, ha='right')

# Set common labels and title
ax1.set_xlabel('Delivery Type')
ax1.set_ylabel('Delivery Days')
plt.title('Delivery Days and Prices')

# Display the legend
ax1.legend(loc='upper left', bbox_to_anchor=(1, 1))
ax2.legend(loc='upper left', bbox_to_anchor=(1, 0.85))

plt.tight_layout()
plt.show()


# Plotting a scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(delivery_days, delivery_prices, color='purple')
plt.title('Scatter Plot: Delivery Days vs Delivery Prices')
plt.xlabel('Delivery Days')
plt.ylabel('Delivery Price (in ₹)')

# Adding labels for each point
for i, txt in enumerate(delivery_types):
    plt.annotate(txt, (delivery_days[i], delivery_prices[i]))

plt.show()
