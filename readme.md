# Car Tire Pressure and Weather 

## Overview of the Project  
This project looks into the connection between tire pressure and weather. My objective is to use regression models to predict changes in tire pressure while accounting for measurable climate and driving-related factors such as temperature, humidity, altitude, and recent driving distance.  

## Motivation
As a person who drives daily to school and other places, I've intended to make use of the time I spend in traveling with my car. With this data, I will be able to see how the tires deprecates through time, including several outer factors.

## Objectives  
- Analyze how different weather patterns affect the tire pressure of a car.
- Identify any potential patterns in pressure loss and suggest better maintenance practices.  

## Information Collection  
The data will be collected manually and will be formed of daily tire pressure readings as well as environmental and vehicle-related factors.  


| Variable | Description |
|----------|-------------|
| `tire_pressure` | Measured tire pressure (PSI) |
| `temperature` | Outside temperature (°C) |
| `altitude` | Elevation above sea level (meters) |
| `car_load_weight` | Approximate weight of passengers/cargo (kg) |
| `driving_distance` | Distance driven before measurement (km) |
| `weather_conditions` | Rainy, Dry, Snowy, Windy |

NOTE: Used data types might differ preciding in the project.

### **Data Sources** 
 **Pressure Data**: Tesla's tire pressure calculator will be used to measure the tire pressure.  
 **Weather Data**: Will be btained through an APIs or mobile weather data apps.  
 **Altitude Data**: Will be obtained by using elevation data from Google Maps or GPS.  
 **Car Load & Distance**: Will be approximated using driving logs of Tesla.  

 ---

 ## Approach  
 1. **Data Collection**: Record tire pressure and environmental information every day.  
 2. **Exploratory Data Analysis (EDA)**: Verify the relationships between tire pressure and meteorological conditions.  
    Recognize changes by season or time of day.  
 3. In order to forecast tire pressure depending on meteorological circumstances, **Regression Modeling** uses **Multiple Linear Regression**.  
    In the event that relationships are non-linear, use polynomial regression.  
 3. **Time Series Regression**: In the event that trends in pressure loss over time are noticed.  
 4. **Model Evaluation**: To evaluate accuracy, use residual analysis, RMSE, and R2 score.  

---

## Anticipation  
A regression model capable of predicting variations in tire pressure awareness of how weather and driving habits impact tire pressure.  

---

## Types of Analysis Performed

- **Univariate Analysis:**  
  - **Histograms** and **boxplots** were used to examine the distribution and basic statistics of individual variables such as tire pressure, temperature, and driving distance.
- **Bivariate Analysis:**  
  - **Scatter plots** and **Pearson correlation coefficients** were used to explore relationships between pairs of variables (e.g., Temperature vs. Tire Pressure).
- **Regression Analysis:**  
  - **Linear regression** and **polynomial regression (degree 2)** models were built to predict tire pressure using temperature and driving distance.
- **Model Evaluation:**  
  - **RMSE** and **R² Score** were used to evaluate model performance. Residual analysis was performed to check for errors and model fit.

**Note:**  
The core analyses performed in this project are univariate, bivariate, and regression analysis with thorough model evaluation. Categorical, multivariate, and trend analyses can be further applied as the dataset grows or more variables are included.


## Analysis Summary & Results

### Correlation Findings

| Variable              | Pearson r | Interpretation                |
|-----------------------|-----------|-------------------------------|
| Temperature (°C)      | 0.851     | Strong positive correlation   |
| Driving Distance (km) | 0.349     | Moderate positive correlation |
| Altitude (m)          | -0.146    | Weak negative correlation     |
| Car Load (kg)         | 0.012     | Negligible correlation        |

- **Temperature** is the primary driver of tire pressure changes.
- **Driving distance** moderately increases tire pressure (likely due to tire heating).
- **Altitude** and **car load** have negligible impact in this dataset.

---

### Regression Model Results

#### Linear Regression

- **RMSE:** 0.948  
- **R²:** 0.713  
- **Intercept:** 35.34  
- **Coefficients:**  
    - Temperature (°C): 0.386  
    - Driving Distance (km): 0.020  

#### Polynomial Regression (Degree 2)

- **RMSE:** 0.957  
- **R²:** 0.707  
- **Intercept:** 35.74  
- **Coefficients:**  
    - Temperature (°C): 0.177  
    - Driving Distance (km): 0.069  
    - Temperature²: 0.009  
    - Temperature × Driving Distance: 0.001  
    - Driving Distance²: -0.001  

> **Comment:**  
> Linear regression performed slightly better than polynomial regression, indicating the relationship between tire pressure and input features is mostly linear. Temperature remains the most influential factor.

---

### Visual Insights

- **Tire Pressure vs. Temperature:**  
  Clear positive linear relationship—higher temperatures yield higher tire pressures.
- **Tire Pressure vs. Distance:**  
  Moderate upward trend, particularly on longer trips.
- **Tire Pressure vs. Altitude/Car Load:**  
  No significant trend.

---

### Conclusion

- **Strongest impact:** Temperature (r = 0.851)
- **Moderate impact:** Driving distance (r = 0.349)
- **Negligible:** Altitude, car load
- **Best model:** Linear Regression (R² = 0.713)
- **Takeaway:**  
  Tire pressure should be checked more often during seasonal temperature changes and after long drives. Regular monitoring can prolong tire lifespan and increase driving safety.

---

### Limitations & Future Work

- **Sample size:** Limited to 1.5 months of daily logs.
- **Weather data:** Manually recorded due to API access limitations.
- **Other variables:** Traffic, road conditions, or tire age not included.

**Planned Improvements:**
- Automate weather data collection with APIs for richer features.
- Collect data over longer periods (multiple seasons).
- Include other variables (road surface, tire age, traffic density).

---

