# Bike Rental Demand Prediction

This project aims to predict and forecast hourly bike rental demand using weather conditions. The goal is to provide accurate demand forecasts for bike-sharing companies to optimize their operations and inventory management. The project uses machine learning models and is deployed as a web application using Streamlit Cloud.

---

## Project Overview

### Problem Statement
The existing research explored various models to improve accuracy by leveraging temporal features like day of the week and month to capture demand patterns but did not focus on the impact of weather conditions such as temperature, humidity, and precipitation, which our project incorporates to enhance demand prediction accuracy.

This project builds a predictive model using weather data to forecast hourly bike rental demand.

**Scope of the Project**

This project aims to predict hourly bike rental demand for two major bike-sharing systems, Capital Bikeshare in Washington D.C. and Citi Bike in New York City, by analyzing the influence of weather conditions. It explores the relationships between weather variables such as temperature, precipitation, and humidity, and their impact on bike rental demand. By utilizing advanced sequential models like Long Short-Term Memory (LSTM) and Recurrent Neural Networks (RNN), the project seeks to capture temporal and environmental patterns in bike usage. The scope extends to comparing demand trends between the two cities to identify geographical and climatic differences. The findings are expected to assist bike-sharing companies in optimizing resource allocation, improving operational efficiency, and enhancing user satisfaction.

### Dataset
The dataset comprises:
1. **Bike Sharing Data**: Contains Capital Bikeshare and Citi Bike data which contains information about ride ids, locations,  ride start times, end times, and stations.
2. **Weather Data**: Temperature, humidity, solar radiation, wind speed, precipitation, and dew point.

The data is sourced from:
- Bike-sharing companies' official datasets (Capital Bikeshare and CitiBike)
- Visual Crossing Weather API for weather data.

Links for Data Sources:

Capital Bikeshare: https://capitalbikeshare.com/

Citi Bike: https://citibikenyc.com/

Weather: Visual Crossing https://www.visualcrossing.com/

### Key Features
- **Total Demand**
- **Hour of the Day**
- **Temperature (°C)**
- **Humidity (%)**
- **Solar Radiation (W/m²)**
- **Wind Speed (km/h)**
- **Precipitation (mm)**
- **Dew Point (°C)**

---

## Machine Learning Models

Traditional Models: Linear regression, KNN, SVR and Decision Trees

Ensemble Models: Random Forest bagging, AdaBoost, XGBoost, GradientBoost and Stacking

Sequential models: Simple RNN, LSTM and GRU

### Evaluation Metrics
- **Mean Absolute Error (MAE)**
- **Mean Squared Error (MSE)**
- **Root Mean Squared Error (RMSE)**
- **R-squared (R²)**

---

## Deployment

## About The App
The project is deployed using **Streamlit Cloud**. This app uses weather data to forecast hourly bike usage for two major bike-sharing services: Capital Bikeshare and Citi Bike. The application allows users to input weather data and predicts the expected bike rental demand.

The application explores how weather conditions—such as temperature, humidity, windspeed, and precipitation—shape bike rental demand. This app delivers actionable insights to optimize resource allocation and enhance service availability.

The app uses Randfom forest model to predict the demand. 

### How to Use the App
1. Input the required weather parameters and hour of the day.
2. Click the **Predict** button.
3. View the predicted bike demand.

---

## Installation of the App

### Prerequisites
- Python 3.8+
- Streamlit
- Required libraries for Streamlit App (listed in `requirements.txt`)

### Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/bikeRentalDemand/StramlitApp.git
   ```
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```bash
   streamlit run streamlitApp/st.py
   ```

## Limitations of the App

The app is not upto date with the real time data from the Capital Bikeshare and Citi Bike Sources. The real time demand may slightly vary from the predicted demand.


---

## Future Work
-  In the future, this project can be expanded to predict bike rental demand by incorporating data from other transportation options like buses, trains, and ride-sharing services.
-  Including factors like traffic conditions and major events can further improve prediction accuracy.
-  Additionally, integrating live data about bike availability at each station can significantly enhance the model's performance.
-  These advancements can help bike-sharing companies and city planners build better-connected and more efficient transportation systems, making urban travel smoother and more convenient for users.
---

## Acknowledgments
- **Citi Bike** and **Capital Bikeshare** for bike-sharing data.
- **Visual Crossing Weather API** for weather data.

---

## Contact
For questions or suggestions, please contact:
- **Venkat Akhil Mothe**: mothevenkatakhil99@gmail.com
- **Dinesh Garampally**: dineshgarampally01@gmail.com
- **Praveen Kumar Keshaboina**: praveenyadavkeshaboina15@gmail.com

