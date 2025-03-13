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
| `humidity` | Humidity level (%) |
| `altitude` | Elevation above sea level (meters) |
| `car_load_weight` | Approximate weight of passengers/cargo (kg) |
| `driving_distance` | Distance driven before measurement (km) |
| `weather_conditions` | Rainy, Dry, Snowy, Windy |
| `surface_type` | Last road driven on (Asphalt, Gravel, Dirt) |

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
