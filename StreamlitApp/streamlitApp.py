import streamlit as st
import pandas as pd
import joblib
from datetime import datetime
import urllib.request
import json
from sklearn.preprocessing import StandardScaler

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
        color: white;
    }
    .error-box {
        color: #b00020;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title
st.markdown('<div class="main-header">Predicting Hourly Bike Rental Demand with Weather Conditions 🚴‍♂️☀️💧</div>', unsafe_allow_html=True)

# Sidebar
st.sidebar.title("Predicting Hourly Bike Rental Demand with Weather Conditions")
st.sidebar.info(
    """
    Welcome to the Bike Rental Demand Prediction Tool! 🚴‍♂️☀️💧

This app leverages weather data to predict hourly bike rental demand for two major bike-sharing services: Capital Bikeshare and Citi Bike.

Explore how weather conditions—such as temperature, humidity, wind speed, and precipitation—influence bike rental demand. Gain actionable insights to optimize resource allocation and ensure seamless service availability.

How It Works:

1. Choose Your City: Select your preferred city from the dropdown.

2. Set Date & Time: Pick a specific date and time for your prediction.

3. Fetch Weather Data: Click the "Fetch Weather Data" button to automatically populate weather details in the input fields.

4. Adjust Weather Values (Optional): You can manually modify the weather details if needed.

5. Predict Demand: Hit "Predict" to get instant insights into hourly bike rental demand.

Ready to predict? Enter the details and see the demand! 🌟
    """
)

# Main section
st.markdown('<div class="sub-header">Select Date, Time, and City</div>', unsafe_allow_html=True)

# City selection dropdown
city_options = {
    "New York, NY, United States (Citi Bike)": "New York, NY",
    "Washington, DC, United States (Capital Bikeshare)": "Washington DC"
}
selected_city = st.selectbox('🌆 Select City', list(city_options.keys()))

# Date and time inputs
today = datetime.today().date()
max_date = today + pd.Timedelta(days=5)

if 'selected_date' not in st.session_state:
    st.session_state.selected_date = today

selected_date = st.date_input('📅 Select Date', st.session_state.selected_date, max_value=max_date)

if selected_date > max_date:
    st.error("You can only select a date within the next 5 days. Please choose a valid date.")
    st.session_state.selected_date = today
    fetch_weather_button_disabled = True
else:
    st.session_state.selected_date = selected_date
    fetch_weather_button_disabled = False

selected_hour = st.slider('🕐 Hour of the Day (0-23)', min_value=0, max_value=23)

# Initializing session state for weather data
for key in ['temp', 'humidity', 'solarradiation', 'dew', 'windspeed', 'precip']:
    if key not in st.session_state:
        st.session_state[key] = 0.0

# "Fetch Weather Data" button
fetch_weather_button = st.button('🌧️ Fetch Weather Data', disabled=fetch_weather_button_disabled)

if fetch_weather_button:
    try:
        city_query = city_options[selected_city]
        api_url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city_query}/{selected_date}/{selected_date}?unitGroup=metric&include=hours&key=9C763VWPH23BCREVNA866DLWV&contentType=json"
        api_url = api_url.replace(" ", "%20")
        print(api_url)
        response = urllib.request.urlopen(api_url)
        weather_data = json.load(response)

        hourly_data = next(
            (hour for hour in weather_data['days'][0]['hours'] if hour['datetime'].startswith(f"{selected_hour:02}:")),
            None
        )

        if hourly_data:
            st.session_state.temp = hourly_data.get('temp', 0.0)
            st.session_state.humidity = hourly_data.get('humidity', 0.0)
            st.session_state.solarradiation = hourly_data.get('solarradiation', 0.0)
            st.session_state.dew = hourly_data.get('dew', 0.0)
            st.session_state.windspeed = hourly_data.get('windspeed', 0.0)
            st.session_state.precip = hourly_data.get('precip', 0.0)
        else:
            st.error("No weather data available for the selected hour.")
    except urllib.error.HTTPError as e:
        if e.code == 401:  # Handle HTTP Error 401 specifically
            st.markdown(
                """
                <div style="
                    color: white; 
                    background-color: #f44336; 
                    padding: 15px; 
                    border-radius: 8px; 
                    margin-top: 20px; 
                    font-size: 16px;
                ">
                    🚫 Limit Exceeded: Please enter values manually. Sorry for the inconvenience☹️
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            st.error("An error occurred while fetching weather data. Please enter values manually.")
    except Exception as e:
        print(e)
        st.error("An error occurred while fetching weather data. Please enter values manually.")

# input fields with fetched or previously entered data
st.markdown('<div class="sub-header">Enter Weather Data</div>', unsafe_allow_html=True)
temp = st.number_input('🌡️ Temperature (°C)', value=st.session_state.temp, min_value=-50.0, max_value=50.0, format="%.2f")
humidity = st.number_input('💧 Humidity (%)', value=st.session_state.humidity, min_value=0.0, max_value=100.0, format="%.2f")
solarradiation = st.number_input('☀️ Solar Radiation (W/m²)', value=st.session_state.solarradiation, min_value=0.0, max_value=2000.0, format="%.2f")
dew = st.number_input('💨 Dew Point (°C)', value=st.session_state.dew, min_value=-50.0, max_value=50.0, format="%.2f")
windspeed = st.number_input('🌬️ Windspeed (km/h)', value=st.session_state.windspeed, min_value=0.0, max_value=150.0, format="%.2f")
precip = st.number_input('🌧️ Precipitation (mm)', value=st.session_state.precip, min_value=0.0, max_value=50.0, format="%.2f")

# Predict button
predict_button = st.button('🔮 Predict Demand', disabled=fetch_weather_button_disabled)

if predict_button:
    try:
        # Checking if all weather inputs are zero
        if all(value == 0.0 for value in [temp, humidity, solarradiation, dew, windspeed, precip]):
            st.markdown(
                """
                <div style="
                    color: white; 
                    background-color: #ff9800; 
                    padding: 15px; 
                    border-radius: 8px; 
                    margin-top: 20px; 
                    font-size: 16px;
                ">
                    ⚠️ Invalid Input: Please enter relevant weather details.
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            if selected_city == "Washington, DC, United States":
                rf_model = joblib.load('StreamlitApp/randomforest_Capitalbike.joblib')
                scaler = joblib.load('StreamlitApp/scaler_Capital.joblib')
            else:
                rf_model = joblib.load('StreamlitApp/randomforest_citibike.joblib')
                scaler = joblib.load('StreamlitApp/scaler_citibike.joblib')

            input_data = pd.DataFrame(
                [[selected_hour, temp, humidity, solarradiation, dew, windspeed, precip]],
                columns=['hour', 'temp', 'humidity', 'solarradiation', 'dew', 'windspeed', 'precip']
            )

            input_scaled = scaler.transform(input_data)
            predicted_demand = rf_model.predict(input_scaled)

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
