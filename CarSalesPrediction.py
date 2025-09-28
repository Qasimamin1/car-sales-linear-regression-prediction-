
import pandas as pd   # import pandas library

# Create sample car sales data (months vs car brands)
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],   # months
    "Mercedes": [2, 4, 5, 7, 6, 8],  # sales numbers
    "Ford": [3, 6, 7, 5, 4, 6],      # sales numbers
    "Tesla": [1, 3, 4, 6, 7, 9]      # sales numbers
}

# Convert dictionary to DataFrame
df = pd.DataFrame(data)   # create DataFrame from dictionary

# Save DataFrame to CSV file
df.to_csv("carsales.csv", index=False)   # save as carsales.csv without index

print("CSV file created successfully!")  # confirmation message
print(df)   # print DataFrame
