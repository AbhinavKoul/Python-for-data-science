# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out first 3 observations
print(cars[:3])

# Print out fourth, fifth and sixth observation
print(cars[3:6])

#if we do
print(cars[3,4,5])       #ERROR as Rows/Observation can only be sliced but not defined as shown