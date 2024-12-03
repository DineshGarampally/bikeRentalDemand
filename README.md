# Bike Rental Demand Prediction

This project aims to predict and forecast hourly bike rental demand using weather conditions. The goal is to provide accurate demand forecasts for bike-sharing companies to optimize their operations and inventory management. The project uses machine learning models and is deployed as a web application using Streamlit Cloud.

---

## Project Overview

### Problem Statement
Bike-sharing companies need to anticipate rental demand to ensure optimal availability of bikes. This project builds a predictive model using weather data to forecast hourly bike rental demand.

### Dataset
The dataset comprises:
1. **Bike Sharing Data**: Contains Capital Bikeshare and Citi Bike data which contains information about ride ids, locations,  ride start times, end times, and stations.
2. **Weather Data**: Temperature, humidity, solar radiation, wind speed, precipitation, and dew point.

The data is sourced from:
- Bike-sharing companies' official datasets (Capital Bikeshare and CitiBike)
- Visual Crossing Weather API for weather data.

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
The project is deployed using **Streamlit Cloud**. The application allows users to input weather data and predicts the expected bike rental demand.

### How to Use the App
1. Input the required weather parameters and hour of the day.
2. Click the **Predict** button.
3. View the predicted bike demand.

---

## Installation

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

---

## Future Work
- Incorporating additional features such as public events or holidays.
- Experimenting with ensemble models for improved performance.
- Extending predictions to multiple cities.

---

## Acknowledgments
- **Citi Bike** and **Capital Bikeshare** for bike-sharing data.
- **Visual Crossing Weather API** for weather data.

---

## Contact
For questions or suggestions, please contact:
- **Venkat Akhil Mothe**: 
- **Dinesh Garampally**: dineshgarampally01@gmail.com
- **Praveen Kumar Keshaboina**: praveenyadavkeshaboina15@gmail.com

