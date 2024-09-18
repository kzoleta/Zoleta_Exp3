#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

#Load the .csv file into a DataFrame named cars
url = "http://bit.ly/Cars_file"  # URL of the CSV file
cars = pd.read_csv(url)

#Display the first five rows
print("First five rows:")
print(cars.head())

#Display the last five rows
print("\nLast five rows:")
print(cars.tail())

