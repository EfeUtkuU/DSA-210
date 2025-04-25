import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

df = pd.read_excel('Tire-Weather Data.xlsx', header=1)
df = df.iloc[:, 1:]
df.columns = [
    "Date", "Tire_Pressure_PSI", "Temperature_F", "Altitude_m",
    "Car_Load_kg", "Driving_Distance_km", "Temperature_C"
]

numericCols = ["Tire_Pressure_PSI", "Temperature_F", "Altitude_m",
                "Car_Load_kg", "Driving_Distance_km", "Temperature_C"]
df[numericCols] = df[numericCols].apply(pd.to_numeric, errors='coerce')
df.dropna(inplace=True)

print("Pearson Correlation Results:")

variablesToPlot = ["Temperature_C", "Temperature_F", "Driving_Distance_km", "Altitude_m", "Car_Load_kg"]

for var in variablesToPlot:
    x = df[var]
    y = df["Tire_Pressure_PSI"]

    r, p_value = stats.pearsonr(x, y)

    print(f"\nVariable: {var}")
    print(f"Pearson Correlation Coefficient: {r:.4f}")
    print(f"p-value: {p_value:.4f}") 

for var in variablesToPlot:
    x = df[var]
    y = df["Tire_Pressure_PSI"]

    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, color='blue', label='Data Points')


    plt.title(f"Tire Pressure vs {var}")
    plt.xlabel(var)
    plt.ylabel("Tire Pressure (PSI)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
