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

### Models Used
1. **Linear Regression **
2. **SVR**
3. **Random Forest Regressor**
4. **XGBoost**
4. **Simple RNN**
5. **LSTM**
6. **GRU**
7. 
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
   git clone https://github.com/bikeRentalDemand.git
   ```
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```bash
   streamlit run app/streamlit_app.py
   ```

---

## Results
- The Random Forest model achieved an **R² score of X.XX** on the test set.
- The LSTM model effectively captured temporal patterns and provided accurate predictions for hourly demand.

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

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

## Contact
For questions or suggestions, please contact:
- **Dinesh**: [Your Email or GitHub Profile]

