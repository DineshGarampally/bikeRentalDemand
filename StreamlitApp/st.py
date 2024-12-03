import streamlit as st
import pandas as pd
import joblib
from datetime import datetime
from sklearn.preprocessing import StandardScaler

# Custom CSS for styling
st.markdown(
    """
    <style>
    body {
        background-color: #f5f7fa;
    }
    .main-header {
        font-size: 32px;
        color: #f54bfa;
        text-align: center;
        margin-bottom: 20px;
    }
    .sub-header {
        font-size: 20px;
        color: #1ac195;
        margin: 10px 0;
    }
    .prediction-box {
        background-color: #50126b;
        padding: 20px;
        border-radius: 8px;
        margin-top: 20px;
        border: 1px solid #cccccc;
    }
    .error-box {
        color: #b00020;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Page Title
st.markdown('<div class="main-header">Predicting Hourly Bike Rental Demand with Weather Conditions 🚴‍♂️☀️💧 🚴‍♂️</div>', unsafe_allow_html=True)

# Sidebar for static information
st.sidebar.title("Predicting Hourly Bike Rental Demand with Weather Conditions 🚴‍♂️☀️💧")
st.sidebar.info(
    """
    Welcome to our bike rental demand prediction tool! This app uses weather data to forecast hourly bike usage for two major bike-sharing services: Capital Bikeshare and Citi Bike.

This application explores how weather conditions—such as temperature, humidity, windspeed, and precipitation—shape bike rental demand. This app delivers actionable insights to optimize resource allocation and enhance service availability.


Ready to predict? Enter the weather details and watch the insights unfold! 🌟
    """
)

# Main section
st.markdown('<div class="sub-header">Enter Weather Data and Time</div>', unsafe_allow_html=True)

# Date and time inputs
selected_date = st.date_input('📅 Select Date', datetime.today())
selected_hour = st.slider('🕒 Hour of the Day (0-23)', min_value=0, max_value=23)

# Weather data inputs
temp = st.number_input('🌡️ Temperature (°C)', value= 0.0, min_value=-50.0, max_value=50.0, format="%.2f", help="Enter the temperature in Celsius.")
humidity = st.number_input('💧 Humidity (%)', value= 0.0, min_value=0.0, max_value=100.0, format="%.2f", help="Enter the percentage humidity.")
solarradiation = st.number_input('☀️ Solar Radiation (W/m²)', min_value=0.0, max_value=2000.0, format="%.2f", help="Solar energy in watts per square meter.")
dew = st.number_input('💨 Dew Point (°C)',value= 0.0, min_value=-50.0, max_value=50.0, format="%.2f", help="The temperature at which dew forms.")
windspeed = st.number_input('🌬️ Windspeed (km/h)', min_value=0.0, max_value=150.0, format="%.2f", help="Wind speed in kilometers per hour.")
precip = st.number_input('🌧️ Precipitation (mm)', min_value=0.0, max_value=50.0, format="%.2f", help="Rainfall in millimeters.")

# Create a "Predict" button
predict_button = st.button('🔮 Predict Demand')


if predict_button:
    # Validate inputs
    if selected_date == datetime(1, 1, 1).date():  # Checks if the selected date is the default invalid date (0000/00/00 equivalent)
        st.error("Please select a valid date.")
    elif selected_hour is None:
        st.error("Hour is required. Please select a valid hour.")
    elif all(v == 0 for v in [temp, humidity, solarradiation, dew, windspeed, precip]):
        st.error("Weather data is required. Please enter valid weather details.")
    else:
        try:
            # Load models and scalers for both services
            rf_model_capital = joblib.load('./randomforest_Capitalbike.joblib')
            scaler_capital = joblib.load('./scaler_Capital.joblib')

            rf_model_citibike = joblib.load('./randomforest_citibike.joblib')
            scaler_citibike = joblib.load('./scaler_citibike.joblib')

            # Prepare the input data
            input_data = pd.DataFrame(
                [[selected_hour, temp, humidity, solarradiation, dew, windspeed, precip]],
                columns=['hour', 'temp', 'humidity', 'solarradiation', 'dew', 'windspeed', 'precip']
            )

            # Scale the input data for each service
            input_scaled_capital = scaler_capital.transform(input_data)
            input_scaled_citibike = scaler_citibike.transform(input_data)

            # Make predictions for both services
            predicted_demand_capital = rf_model_capital.predict(input_scaled_capital)
            predicted_demand_citibike = rf_model_citibike.predict(input_scaled_citibike)

            # Display the results
            prediction_datetime = datetime.combine(selected_date, datetime.min.time()) + pd.Timedelta(hours=selected_hour)
            predicted_demand_capital_rounded = round(predicted_demand_capital[0])
            predicted_demand_citibike_rounded = round(predicted_demand_citibike[0])
            col1, col2 = st.columns(2)

            with col1:
                st.markdown(
                    f'<div class="prediction-box">'
                    f'<h3>🚴‍♂️ Capital Bikeshare Prediction</h3>'
                    f'<p><strong>Date and Time:</strong> {prediction_datetime.strftime("%Y-%m-%d %H:%M:%S")}</p>'
                    f'<p><strong>Total Demand:</strong> {predicted_demand_capital_rounded}</p>'
                    f'</div>',
                    unsafe_allow_html=True,
                )

            with col2:
                st.markdown(
                    f'<div class="prediction-box">'
                    f'<h3>🚴‍♀️ Citi Bike Prediction</h3>'
                    f'<p><strong>Date and Time:</strong> {prediction_datetime.strftime("%Y-%m-%d %H:%M:%S")}</p>'
                    f'<p><strong>Total Demand:</strong> {predicted_demand_citibike_rounded}</p>'
                    f'</div>',
                    unsafe_allow_html=True,
                )
        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")
