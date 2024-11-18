import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import glob
import tkinter as tk
from tkinter import messagebox
from tkinter import messagebox, ttk 

# List of CSV files to process
csv_files = glob.glob('/Users/kamsy/Downloads/realtor-data.zip.csv')  

# Data aggregation
all_data = pd.DataFrame()

# Loop through each CSV file, load and clean the data, and append it to `all_data`
for file in csv_files:
    data = pd.read_csv(file)

    # Select and rename relevant columns
    if 'status' in data.columns and 'price' in data.columns:
        data = data[['status', 'price', 'bed', 'bath', 'acre_lot', 'street', 'city', 'state', 'zip_code']]
        data.columns = ['Status', 'Price', 'Bedrooms', 'Bathrooms', 'Acre_Lot', 'Street', 'City', 'State', 'Zip_Code']
    else:
        print(f"File {file} does not contain the necessary columns.")
        continue

    # Data Cleaning
    data.dropna(inplace=True)  # Drop rows with NaN values
    data['Price'] = pd.to_numeric(data['Price'], errors='coerce')  # Ensure 'Price' is numeric
    data.dropna(subset=['Price'], inplace=True)  # Remove rows with non-numeric prices

    # Append cleaned data to all_data
    all_data = pd.concat([all_data, data], ignore_index=True)

print("Loading...")

# Check if 'Price' column exists in `all_data`
if 'Price' not in all_data.columns:
    raise KeyError("The 'Price' column is missing from the aggregated data. Check data processing steps.")

# Sorting and duplicates handling (if needed)
all_data.drop_duplicates(inplace=True)

# Generate a numerical "Days" column to simulate time progression for analysis
all_data['Days'] = np.arange(len(all_data))

# Prepare data for polynomial fitting
x = all_data['Days'].values
y = all_data['Price'].values

# Remove any NaN or Inf values
valid_indices = np.isfinite(x) & np.isfinite(y)
x = x[valid_indices]
y = y[valid_indices]

# Polynomial fitting
poly_degree = 6
if len(x) > poly_degree:
    try:
        coefficients = np.polyfit(x, y, poly_degree)
        trend_function = np.poly1d(coefficients)
    except np.linalg.LinAlgError:
        print("Polynomial fit did not converge. Reducing polynomial degree to 10.")
        poly_degree = 4
        coefficients = np.polyfit(x, y, poly_degree)
        trend_function = np.poly1d(coefficients)
else:
    print("Not enough data points to fit the specified polynomial degree.")
    trend_function = None

# Calculate turning points using the second derivative
turning_points = []
if trend_function:
    second_derivative = np.polyder(trend_function, 2)
    for i in range(1, len(x)):
        if (second_derivative(x[i-1]) > 0 and second_derivative(x[i]) < 0) or (second_derivative(x[i-1]) < 0 and second_derivative(x[i]) > 0):
            turning_points.append(i)

# Model Training for Prediction
X = all_data[['Days']].values
y = all_data['Price'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

model = LinearRegression()
model.fit(X_train, y_train)
print(f"Model R^2 Score on Test Data: {model.score(X_test, y_test):.2f}")

# Enhanced function to predict price on a given future day count
def predict_price(days_ahead):
    if days_ahead < 0:
        return "Please provide a positive integer for days ahead."

    if trend_function and model:
        # Calculate the day count for prediction based on existing data
        future_days = all_data['Days'].max() + days_ahead

        # Use linear model prediction
        linear_pred = model.predict([[future_days]])

        # Use polynomial trend if available
        poly_pred = trend_function(future_days)

        # Calculate the change from the latest known price
        latest_price = all_data['Price'].iloc[-1]
        change_percent = ((poly_pred - latest_price) / latest_price) * 100

        return {
            "Predicted Price (Linear)": round(linear_pred[0], 2),
            "Predicted Price (Trend)": round(poly_pred, 2),
            "Change from Latest Price (%)": round(change_percent, 2)
        }
    else:
        return "Prediction unavailable due to insufficient data."

# Function to run analysis and display results in Tkinter
def run_analysis():
    try:
        days_ahead = int(entry_days.get())
        predicted_price = predict_price(days_ahead)

        # Prepare output string
        if isinstance(predicted_price, dict):
            output = f"The predicted property prices in {days_ahead} days are:\n"
            for key, value in predicted_price.items():
                output += f"{key}: {value}\n"
        else:
            output = predicted_price

        # Display output in message box
        messagebox.showinfo("Prediction Result", output)

        # Visualization
        plt.figure(figsize=(12, 8))
        plt.plot(all_data['Days'], all_data['Price'], label='Historical Prices', color='blue', linewidth=2.0)
        if trend_function:
            days_range = np.linspace(all_data['Days'].min(), all_data['Days'].max(), 100)
            trend_values = trend_function(days_range)
            plt.plot(days_range, trend_values, label=f'{poly_degree}° Polynomial Trend', color='orange', linestyle='-')

        # Plotting turning points
        for point in turning_points:
            plt.plot(point, trend_function(point), 'ro', label='Turning Point' if point == turning_points[0] else "", markersize=8)

        plt.xlim(0, 3650)
        plt.ylim(0, 30000000)
        plt.xlabel("Days")
        plt.ylabel("Price (x10^7)")
        plt.title("Property Price Analysis: Historical Prices, Trend, and Turning Points")
        plt.legend()
        plt.grid(True)
        plt.show()

    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid integer for days ahead.")

# Create the main window
root = tk.Tk()
root.title("Property Price Prediction")
root.geometry("1200x800")  # Set a larger window size
root.configure(bg='#2E3B4E')  # Darker background for a professional look

# Header
header_frame = tk.Frame(root, bg='#2E3B4E')
header_frame.pack(fill=tk.X, pady=10)

title_label = tk.Label(header_frame, text="Property Price Prediction Tool", font=("Arial", 26, "bold"), fg='white', bg='#2E3B4E')
title_label.pack()

# Main content frame for layout management
content_frame = tk.Frame(root, bg='#f0f0f0')
content_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

# Left panel for inputs
input_panel = ttk.Frame(content_frame, padding="20")
input_panel.grid(row=0, column=0, sticky="nsew", padx=(0, 10), pady=10)

input_title = tk.Label(input_panel, text="Input Parameters", font=("Arial", 18, "bold"), bg='#f0f0f0')
input_title.pack(pady=(0, 10))

# Days input field
label_days = tk.Label(input_panel, text="Enter the number of days ahead for prediction:", font=("Arial", 14), bg='#f0f0f0')
label_days.pack(anchor='w', pady=5)

entry_days = tk.Entry(input_panel, font=("Arial", 14), width=10)
entry_days.pack(pady=(0, 20))

# Run analysis button
button = tk.Button(input_panel, text="Run Analysis", command=run_analysis, font=("Arial", 14), bg='#4CAF50', fg='white', activebackground='#45a049')
button.pack(pady=(10, 20))

# Right panel for displaying results
results_panel = ttk.Frame(content_frame, padding="20")
results_panel.grid(row=0, column=1, sticky="nsew", padx=(10, 0), pady=10)

results_title = tk.Label(results_panel, text="Analysis Results", font=("Arial", 18, "bold"), bg='#f0f0f0')
results_title.pack(pady=(0, 10))

# Results display label
results_label = tk.Label(results_panel, text="Prediction results will be displayed here.", font=("Arial", 14), bg='#f0f0f0', anchor='nw', justify='left', wraplength=500)
results_label.pack(fill=tk.BOTH, expand=True)

# Footer
footer_frame = tk.Frame(root, bg='#2E3B4E')
footer_frame.pack(fill=tk.X)

footer_label = tk.Label(footer_frame, text="© 2024 Property Price Prediction Tool", font=("Arial", 10), fg='white', bg='#2E3B4E')
footer_label.pack(side=tk.BOTTOM, pady=10)

# Configure grid weights for responsiveness
content_frame.grid_columnconfigure(0, weight=1)
content_frame.grid_columnconfigure(1, weight=1)
content_frame.grid_rowconfigure(0, weight=1)

# Run the Tkinter event loop
root.mainloop()