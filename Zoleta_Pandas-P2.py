#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

#Input validation for loading the CSV file
try:
    url = "http://bit.ly/Cars_file"
    cars = pd.read_csv(url)

    if cars.empty:
        raise ValueError("The CSV file is loaded, but it is empty.")
    
    #Display the first five rows with odd-numbered columns
    print(cars.iloc[:5, ::2])  # :5 for first 5 rows, ::2 to skip columns

    #Display the row with Mazda RX4
    mazda_rx4 = cars[cars['Model'] == 'Mazda RX4']
    if mazda_rx4.empty:
        print("No car with model 'Mazda RX4' found.")
    else:
        print("\nRow with Model 'Mazda RX4':")
        print(mazda_rx4)
    
    #Camaro Z28 cylinders
    camaro_z28 = cars[cars['Model'] == 'Camaro Z28']
    if camaro_z28.empty:
        print("No car with model 'Camaro Z28' found.")
    else:
        cyl_camaro = camaro_z28['cyl'].values[0]
        print(f"\nThe 'Camaro Z28' has {cyl_camaro} cylinders.")
    
    #Determine cylinders and gear type for selected models
    selected_models = cars[cars['Model'].isin(['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic'])]
    if selected_models.empty:
        print("No cars found for the selected models.")
    else:
        print("\nCylinders and Gear type for 'Mazda RX4 Wag', 'Ford Pantera L', and 'Honda Civic':")
        print(selected_models[['Model', 'cyl', 'gear']])

except pd.errors.ParserError as e:
    print("Error parsing the CSV file:", e)
except FileNotFoundError:
    print("The CSV file could not be found.")
except Exception as e:
    print("An error occurred:", e)

