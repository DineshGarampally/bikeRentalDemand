# Bike Rental Demand Prediction

This project aims to predict and forecast hourly bike rental demand using weather conditions. The goal is to provide accurate demand forecasts for bike-sharing companies to optimize their operations and inventory management. The project uses machine learning models and is deployed as a web application using Streamlit Cloud.


## Problem Statement
The existing research explored various models to improve accuracy by leveraging temporal features like day of the week and month to capture demand patterns but did not focus on the impact of weather conditions such as temperature, humidity, and precipitation, which our project incorporates to enhance demand prediction accuracy.

This project builds a predictive model using weather data to forecast hourly bike rental demand.

## Scope of the Project

This project aims to predict hourly bike rental demand for two major bike-sharing systems, Capital Bikeshare in Washington D.C. and Citi Bike in New York City, by analyzing the influence of weather conditions. It explores the relationships between weather variables such as temperature, precipitation, and humidity, and their impact on bike rental demand. By utilizing advanced sequential models like Long Short-Term Memory (LSTM) and Recurrent Neural Networks (RNN), the project seeks to capture temporal and environmental patterns in bike usage. The scope extends to comparing demand trends between the two cities to identify geographical and climatic differences. The findings are expected to assist bike-sharing companies in optimizing resource allocation, improving operational efficiency, and enhancing user satisfaction.

## Dataset
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

## Key Features
- Total Demand
- Hour of the Day
- Temperature (°C)
- Humidity (%)
- Solar Radiation (W/m²)
- Wind Speed (km/h)
- Precipitation (mm)
- Dew Point (°C)

## Machine Learning Models

**Traditional Models:** Linear regression, KNN, SVR and Decision Trees

**Ensemble Models:** Random Forest bagging, AdaBoost, XGBoost, GradientBoost and Stacking

**Sequential models:** Simple RNN, LSTM and GRU

### Evaluation Metrics
- **Mean Absolute Error (MAE)**
- **Mean Squared Error (MSE)**
- **Root Mean Squared Error (RMSE)**
- **R-squared (R²)**


## How to Run the Python File (BikeRentalDemand.ipynb)

Follow the steps below to set up and run the notebook:

**1. Download Necessary Datasets**

**Capital Bikeshare Data:**
Download data for the months you are interested in.
For this project, we used data from July 2023 to August 2024.

**Citi Bike Data:**
Download data for the months you are interested in.
For this project, we used data from April 2023 to April 2024.

**Weather Data:**
Download the weather data from the provided datasets folder in this repository.

**2. Update File Paths in the Notebook**

Update the file paths in the BikeRentalDemand.ipynb notebook to match the location of your downloaded files.
If you are running the notebook locally, you can remove the Google Drive authentication and authorization steps at the start of the notebook.

**3. Run the Notebook**

Execute the cells in the notebook sequentially to:

Load and preprocess the data.

Train the machine learning models.

Evaluate the model's performance.

## Deployment

**About The App**

The project is deployed using **Streamlit Cloud**. This app uses weather data to forecast hourly bike usage for two major bike-sharing services: Capital Bikeshare and Citi Bike. The application allows users to input weather data and predicts the expected bike rental demand.

The application explores how weather conditions—such as temperature, humidity, windspeed, and precipitation—shape bike rental demand. This app delivers actionable insights to optimize resource allocation and enhance service availability.

The app uses Pre Trained Randfom forest model to predict the demand. 

**How to Use the App**

1. Choose Your City: Select your preferred city from the dropdown.

2. Set Date & Time: Pick a specific date and time for your prediction.

3. Fetch Weather Data: Click the "Fetch Weather Data" button to automatically populate weather details in the input fields.

4. Adjust Weather Values (Optional): You can manually modify the weather details if needed.

Predict Demand: Hit "Predict" to get instant insights into hourly bike rental demand.

**Installation of the App**

**Prerequisites**
- Python 3.8+
- Streamlit
- Required libraries for Streamlit App (listed in `requirements.txt`)

**Steps**
1. Clone this repository:
   ```bash
   git clone https://github.com/bikeRentalDemand/StreamlitApp.git
   ```
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```bash
   streamlit run streamlitApp/streamlitApp.py
   ```
## Screenshots

<img width="1234" alt="image" src="https://github.com/user-attachments/assets/458056ac-5733-4dc6-b5ef-ebf1eadb2387">
<br>
<img width="634" alt="image" src="https://github.com/user-attachments/assets/a8602a40-1992-4424-b61d-93a06ba1d9e6">
<br>
<img width="646" alt="image" src="https://github.com/user-attachments/assets/69449d26-d17c-417f-be3a-f382a2a9ecaa">

## Limitations of the App

**Real-Time Data Unavailability:** The app does not integrate with real-time data from Capital Bikeshare and Citi Bike sources. As a result, actual demand may slightly differ from the predicted demand.

**API Call Limitations:** The app relies on weather data fetched via an API, which has a daily limit on the number of calls. If the limit is exceeded or if there are issues fetching data, users are encouraged to enter the required values manually until the problem is resolved.


## Future Work
-  In the future, this project can be expanded to predict bike rental demand by incorporating data from other transportation options like buses, trains, and ride-sharing services.
-  Including factors like traffic conditions and major events can further improve prediction accuracy.
-  Additionally, integrating live data about bike availability at each station can significantly enhance the model's performance and also users experience.
-  These advancements can help bike-sharing companies and city planners build better-connected and more efficient transportation systems, making urban travel smoother and more convenient for users.
   
## Acknowledgments
- **Citi Bike** and **Capital Bikeshare** for bike-sharing data.
- **Visual Crossing Weather API** for weather data.


## Contact
For questions or suggestions, please contact:
- **Dinesh Garampally**: dineshgarampally01@gmail.com
- **Praveen Kumar Keshaboina**: praveenyadavkeshaboina15@gmail.com
- **Venkat Akhil Mothe**: mothevenkatakhil99@gmail.com

