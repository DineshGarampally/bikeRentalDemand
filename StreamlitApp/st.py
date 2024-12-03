import streamlit as st
import pandas as pd
import joblib
from datetime import datetime
from sklearn.preprocessing import StandardScaler

# Load the trained Random Forest model and scaler
rf_model = joblib.load('StreamlitApp/randomforest.joblib')
scaler = joblib.load('./scaler.joblib')

# Custom CSS for styling
st.markdown(
    """
    <style>
    body {
        background-color: #f5f7fa;
    }
    .main-header {
        font-size: 32px;
        color: #333333;
        text-align: center;
        margin-bottom: 20px;
    }
    .sub-header {
        font-size: 20px;
        color: #666666;
        margin-top: 10px;
    }
    .prediction-box {
        background-color: #499cde;
        padding: 20px;
        border-radius: 8px;
        margin-top: 20px;
        border: 1px solid #90caf9;
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
st.markdown('<div class="main-header">Bike Demand Prediction 🚴‍♂️</div>', unsafe_allow_html=True)

# Sidebar for static information
st.sidebar.title("Bike Prediction App Info")
st.sidebar.info(
    """
    Enter weather details and select a date/time to predict bike demand. 
    This app uses a pre-trained Random Forest model.
    """
)

# Main section
st.markdown('<div class="sub-header">Enter Weather Data and Time:</div>', unsafe_allow_html=True)

# Date and time inputs
selected_date = st.date_input('📅 Select Date', datetime.today())
selected_hour = st.slider('🕒 Hour of the Day (0-23)', min_value=0, max_value=23)

# Weather data inputs
temp = st.number_input('🌡️ Temperature (°C)', min_value=-50.0, max_value=50.0, format="%.2f", help="Enter the temperature in Celsius.")
humidity = st.number_input('💧 Humidity (%)', min_value=0.0, max_value=100.0, format="%.2f", help="Enter the percentage humidity.")
solarradiation = st.number_input('☀️ Solar Radiation (W/m²)', min_value=0.0, max_value=2000.0, format="%.2f", help="Solar energy in watts per square meter.")
dew = st.number_input('💨 Dew Point (°C)', min_value=-50.0, max_value=50.0, format="%.2f", help="The temperature at which dew forms.")
windspeed = st.number_input('🌬️ Windspeed (km/h)', min_value=0.0, max_value=150.0, format="%.2f", help="Wind speed in kilometers per hour.")
precip = st.number_input('🌧️ Precipitation (mm)', min_value=0.0, max_value=50.0, format="%.2f", help="Rainfall in millimeters.")

# Create a "Predict" button
predict_button = st.button('🔮 Predict Demand')

if predict_button:
    # Validate inputs
    if selected_date is None:
        st.error("Date is required. Please select a valid date.")
    elif all(v == 0 for v in [temp, humidity, solarradiation, dew, windspeed, precip]) and selected_hour == 0:
        st.error("All input fields cannot be zero. Please enter valid weather details.")
    else:
        try:
            # Prepare the input data
            input_data = pd.DataFrame(
                [[selected_hour, temp, humidity, solarradiation, dew, windspeed, precip]],
                columns=['hour', 'temp', 'humidity', 'solarradiation', 'dew', 'windspeed', 'precip']
            )

            # Scale the input data
            input_scaled = scaler.transform(input_data)

            # Make prediction
            predicted_demand = rf_model.predict(input_scaled)

            # Display the results
            prediction_datetime = datetime.combine(selected_date, datetime.min.time()) + pd.Timedelta(hours=selected_hour)
            st.markdown(
                f'<div class="prediction-box">'
                f'<h3>🚴‍♂️ Predicted Bike Demand:</h3>'
                f'<p><strong>Date and Time:</strong> {prediction_datetime.strftime("%Y-%m-%d %H:%M:%S")}</p>'
                f'<p><strong>Total Demand:</strong> {predicted_demand[0]:.2f}</p>'
                f'</div>',
                unsafe_allow_html=True,
            )
        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")
