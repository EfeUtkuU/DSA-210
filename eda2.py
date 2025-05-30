import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel('Tire-Weather Data.xlsx', header=1)
df = df.iloc[:, 1:]
df.columns = [
    "Date", "Tire_Pressure_PSI", "Temperature_F", "Altitude_m",
    "Car_Load_kg", "Driving_Distance_km", "Temperature_C"
]

# 1. Tire Pressure Histogram
plt.figure(figsize=(6,4))
plt.hist(df['Tire_Pressure_PSI'], bins=12, edgecolor='black', alpha=0.7)
plt.title('Tire Pressure Distribution')
plt.xlabel('Tire Pressure (PSI)')
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.show()

# 2. Tire Pressure Boxplot
plt.figure(figsize=(4,4))
plt.boxplot(df['Tire_Pressure_PSI'], vert=True)
plt.title('Boxplot of Tire Pressure')
plt.ylabel('Tire Pressure (PSI)')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.show()

# 3. Scatter: Temperature (C) vs Tire Pressure
plt.figure(figsize=(6,4))
plt.scatter(df['Temperature_C'], df['Tire_Pressure_PSI'], alpha=0.8)
plt.title('Tire Pressure vs Temperature (C)')
plt.xlabel('Average Daily Temperature (°C)')
plt.ylabel('Tire Pressure (PSI)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()

# 4. Scatter: Driving Distance vs Tire Pressure
plt.figure(figsize=(6,4))
plt.scatter(df['Driving_Distance_km'], df['Tire_Pressure_PSI'], alpha=0.8)
plt.title('Tire Pressure vs Driving Distance')
plt.xlabel('Driving Distance (km)')
plt.ylabel('Tire Pressure (PSI)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()

# 5. Basit Correlation Matrix Heatmap (matplotlib ile)
cols = [
    'Tire_Pressure_PSI', 'Temperature_C', 'Driving_Distance_km',
    'Altitude_m', 'Car_Load_kg'
]
corr = df[cols].corr()
fig, ax = plt.subplots(figsize=(6,5))
cax = ax.matshow(corr, cmap='coolwarm')
plt.xticks(range(len(cols)), cols, rotation=45)
plt.yticks(range(len(cols)), cols)
for (i, j), val in np.ndenumerate(corr.round(2)):
    ax.text(j, i, str(val), ha='center', va='center', color='white' if abs(val) > 0.5 else 'black')
fig.colorbar(cax)
plt.title('Correlation Matrix', pad=20)
plt.tight_layout()
plt.show()

# 6. Line Plot: Tire Pressure Over Time
df['Date'] = pd.to_datetime(df['Date'])
df_sorted = df.sort_values('Date')
plt.figure(figsize=(10,4))
plt.plot(df_sorted['Date'], df_sorted['Tire_Pressure_PSI'], marker='o')
plt.title('Tire Pressure Over Time')
plt.xlabel('Date')
plt.ylabel('Tire Pressure (PSI)')
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
