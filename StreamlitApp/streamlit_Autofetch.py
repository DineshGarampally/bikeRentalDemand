import streamlit as st
import pandas as pd
import joblib
from datetime import datetime
import urllib.request
import json
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
st.sidebar.title("Predicting Hourly Bike Rental Demand")
st.sidebar.info(
    """
    Welcome to our bike rental demand prediction tool! This app uses weather data to forecast hourly bike usage for two major bike-sharing services: Capital Bikeshare and Citi Bike.

    Ready to predict? Enter the details and watch the insights unfold! 🌟
    """
)

# Main section
st.markdown('<div class="sub-header">Select Date, Time, and City</div>', unsafe_allow_html=True)

# City selection dropdown
city_options = {
    "New York, NY, United States": "New York, NY",
    "Washington, DC, United States": "Washington DC"
}
selected_city = st.selectbox('🌆 Select City', list(city_options.keys()))

# Date and time inputs
today = datetime.today().date()  # Use only the date part
max_date = today + pd.Timedelta(days=5)  # Set the maximum allowable date to 5 days from today

# Initialize the selected_date in session state if not already set
if 'selected_date' not in st.session_state:
    st.session_state.selected_date = today

# Date input validation
selected_date = st.date_input('📅 Select Date', st.session_state.selected_date, max_value=max_date)

# Check if the selected date is more than 5 days in the future or in the past
if selected_date > max_date:
    st.error("You can only select a date within the next 5 days. Please choose a valid date.")
    # Reset the selected date to today's date in session state
    st.session_state.selected_date = today
    # Disable the "Fetch Weather Data" button
    fetch_weather_button_disabled = True
else:
    # Update the session state with the valid selected date
    st.session_state.selected_date = selected_date
    # Enable the "Fetch Weather Data" button
    fetch_weather_button_disabled = False
    
selected_hour = st.slider('🕐 Hour of the Day (0-23)', min_value=0, max_value=23)
# Initialize default values for weather data variables
temp = 0.0
humidity = 0.0
solarradiation = 0.0
dew = 0.0
windspeed = 0.0
precip = 0.0

# Create a "Fetch Weather Data" button
fetch_weather_button = st.button('🌧️ Fetch Weather Data', disabled=fetch_weather_button_disabled)
# Weather data fields

if fetch_weather_button:
    try:
        city_query = city_options[selected_city]
        api_url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city_query}/{selected_date}/{selected_date}?unitGroup=metric&include=hours&key=DH8GA73VZKYRFVNMVP9DLG8PC&contentType=json"
        api_url = api_url.replace(" ", "%20")  # Encode spaces in the URL
        print(api_url)
        response = urllib.request.urlopen(api_url)
        weather_data = json.load(response)
        print(response)
        print(weather_data)
        
        # Extract hourly weather data for the selected hour
        hourly_data = None
        for hour in weather_data['days'][0]['hours']:
            if hour['datetime'].startswith(f"{selected_hour:02}:"):  # Check if the hour matches
                hourly_data = hour
                break

        if hourly_data:
            # Extract relevant weather data from the matched hour
            temp = hourly_data.get('temp', 0.0)
            humidity = hourly_data.get('humidity', 0.0)
            solarradiation = hourly_data.get('solarradiation', 0.0)
            dew = hourly_data.get('dew', 0.0)
            windspeed = hourly_data.get('windspeed', 0.0)
            precip = hourly_data.get('precip', 0.0)
        else:
            st.error("No weather data available for the selected hour.")

    except Exception as e:
        st.error(f"An error occurred while fetching weather data: {e}")

# Show input fields with fetched data
st.markdown('<div class="sub-header">Enter Weather Data</div>', unsafe_allow_html=True)
temp = st.number_input('🌡️ Temperature (°C)', value=temp, min_value=-50.0, max_value=50.0, format="%.2f")
humidity = st.number_input('💧 Humidity (%)', value=humidity, min_value=0.0, max_value=100.0, format="%.2f")
solarradiation = st.number_input('☀️ Solar Radiation (W/m²)', value=solarradiation, min_value=0.0, max_value=2000.0, format="%.2f")
dew = st.number_input('💨 Dew Point (°C)', value=dew, min_value=-50.0, max_value=50.0, format="%.2f")
windspeed = st.number_input('🌬️ Windspeed (km/h)', value=windspeed, min_value=0.0, max_value=150.0, format="%.2f")
precip = st.number_input('🌧️ Precipitation (mm)', value=precip, min_value=0.0, max_value=50.0, format="%.2f")

# Predict button
predict_button = st.button('🔮 Predict Demand', disabled=fetch_weather_button_disabled)

if predict_button:
    try:
        if selected_city == "Washington, DC, United States":
            # Load Washington DC model and scaler
            rf_model = joblib.load('StreamlitApp/randomforest_Capitalbike.joblib')
            scaler = joblib.load('StreamlitApp/scaler_Capital.joblib')
        else:
            # Load New York City model and scaler
            rf_model = joblib.load('StreamlitApp/randomforest_citibike.joblib')
            scaler = joblib.load('StreamlitApp/scaler_Citibike.joblib')

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
        predicted_demand_rounded = round(predicted_demand[0])

        st.markdown(
            f'<div class="prediction-box">'
            f'<h3>🚴‍♂️ {selected_city} Prediction</h3>'
            f'<p><strong>Date and Time:</strong> {prediction_datetime.strftime("%Y-%m-%d %H:%M:%S")}</p>'
            f'<p><strong>Total Demand:</strong> {predicted_demand_rounded}</p>'
            f'</div>',
            unsafe_allow_html=True,
        )

    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")
