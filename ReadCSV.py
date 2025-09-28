import pandas as pd   # import pandas library

# Step 3: Load the CSV file
df = pd.read_csv("carsales.csv")   # read the CSV

print("CSV data loaded:\n")
print(df)   # show all data

# Filter only Tesla sales
print("\nTesla sales only:\n")
print(df[["Month", "Tesla"]])   # select Month + Tesla column

# Calculate total sales per brand
print("\nTotal sales per brand:")
print(df[["Mercedes", "Ford", "Tesla"]].sum())   # sum column values

# Calculate average sales per brand
print("\nAverage sales per brand:")
print(df[["Mercedes", "Ford", "Tesla"]].mean())  # mean column values
