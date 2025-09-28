import pandas as pd               # for data handling
from sklearn.linear_model import LinearRegression   # for ML model

# Step 4: Load the CSV file
df = pd.read_csv("carsales.csv")   # load sales data
print("Original Data:\n", df)

# Convert Month names to numbers (Jan=1, Feb=2, ..., Jun=6)
month_map = {"Jan":1, "Feb":2, "Mar":3, "Apr":4, "May":5, "Jun":6}
df["Month_num"] = df["Month"].map(month_map)

# Prepare X (months)
X = df[["Month_num"]]   # independent variable (months)

brands = ["Mercedes", "Ford", "Tesla"]

print("\n--- Predictions for July (Month 7) ---")

# Dictionary to store predictions
predictions = {"Month": ["July"]}

# Train and predict for each brand
for brand in brands:
    y = df[brand]                      # sales for this brand
    model = LinearRegression()         # create model
    model.fit(X, y)                    # train model
    # FIX: use DataFrame with correct column name to avoid warnings
    prediction = model.predict(pd.DataFrame([[7]], columns=["Month_num"]))
    print(f"{brand}: {prediction[0]:.2f} cars")
    predictions[brand] = [round(prediction[0], 2)]  # save to dictionary

# Convert dictionary to DataFrame
pred_df = pd.DataFrame(predictions)

# Save predictions to CSV
pred_df.to_csv("sales_predictions.csv", index=False)

print("\nPredictions saved to 'sales_predictions.csv':\n")
print(pred_df)
