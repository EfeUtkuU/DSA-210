
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

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

x_col = 'Temperature_C'
y_col = 'Driving_Distance_km'
target_col = 'Tire_Pressure_PSI'

X = df[[x_col, y_col]]
y = df[target_col]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)
y_pred_lin = lin_reg.predict(X_test)

rmse_lin = np.sqrt(mean_squared_error(y_test, y_pred_lin))
r2_lin = r2_score(y_test, y_pred_lin)

print("==== Linear Regression ====")
print(f"RMSE: {rmse_lin:.3f}")
print(f"R²: {r2_lin:.3f}")
print("Intercept:", lin_reg.intercept_)
for name, coef in zip([x_col, y_col], lin_reg.coef_):
    print(f"{name}: {coef:.3f}")

poly = PolynomialFeatures(degree=2, include_bias=False)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

poly_reg = LinearRegression()
poly_reg.fit(X_train_poly, y_train)
y_pred_poly = poly_reg.predict(X_test_poly)

rmse_poly = np.sqrt(mean_squared_error(y_test, y_pred_poly))
r2_poly = r2_score(y_test, y_pred_poly)

print("\n==== Polynomial Regression (degree 2) ====")
print(f"RMSE: {rmse_poly:.3f}")
print(f"R²: {r2_poly:.3f}")
print("Intercept:", poly_reg.intercept_)
for name, coef in zip(poly.get_feature_names_out([x_col, y_col]), poly_reg.coef_):
    print(f"{name}: {coef:.3f}")

plt.scatter(y_test, y_pred_lin, label='Linear', alpha=0.7)
plt.scatter(y_test, y_pred_poly, label='Polynomial (deg 2)', alpha=0.7)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
plt.xlabel('Actual Tire Pressure (PSI)')
plt.ylabel('Predicted Tire Pressure (PSI)')
plt.legend()
plt.title('Model Predictions vs. Actual')
plt.tight_layout()
plt.show()
