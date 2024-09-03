import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load the pre-trained model, scaler, and feature columns
model = joblib.load(r"C:\Users\Lenovo\Desktop\final_project\car_insurance\Sourse\best_model.pkl")
scaler = joblib.load(r"C:\Users\Lenovo\Desktop\final_project\car_insurance\Sourse\scaler.pkl")
feature_columns = joblib.load(r"C:\Users\Lenovo\Desktop\final_project\car_insurance\Sourse\feature_columns.pkl")

# Streamlit app title
st.title('Car Insurance Claim Prediction')

# Input fields
policy_tenure = st.number_input("What is the duration of your car insurance policy (in years)?")
age_of_car = st.number_input("What is the age of your car (in years)?")
age_of_policyholder = st.number_input("What is the age of the policyholder (in years)?", min_value=18, value=18)
length = st.number_input("What is the length of your car (in millimeters)?", min_value=1000, value=3000)
width = st.number_input("What is the width of your car (in millimeters)?", min_value=1000, value=1500)
height = st.number_input("What is the height of your car (in millimeters)?", min_value=1000, value=1500)
ncap_rating = st.selectbox("What is the NCAP safety rating of your car?", options=[0, 1, 2, 3, 4, 5], index=0)
segment = st.selectbox("What is the segment of your car?", options=['A', 'B1', 'B2', 'C1', 'C2', 'Utility'], index=0)
fuel_type = st.selectbox("What is the type of fuel does your car use?", options=['CNG', 'Petrol', 'Diesel'], index=0)
max_torque = st.number_input("What is the maximum torque generated by your car (in Nm)?", min_value=0, value=0)
max_power = st.number_input("What is the maximum power generated by your car (in bhp)?", min_value=0, value=0)
airbags = st.selectbox("How many airbags does your car have?", options=[1, 2, 6], index=0)
rear_brakes_type = st.selectbox("What type of rear brakes does your car have?", options=['Drum', 'Disc'], index=0)
cylinder = st.selectbox("How many cylinders does your car engine have?", options=[3, 4], index=1)
transmission_type = st.selectbox("What is the transmission type of your car?", options=['Manual', 'Automatic'], index=0)
gear_box = st.selectbox("How many gears does the gearbox of your car have?", options=[5, 6], index=0)
steering_type = st.selectbox("What type of steering does your car have?", options=['Power', 'Electric', 'Manual'], index=0)
gross_weight = st.number_input("What is the gross weight of your car (in kg)?", min_value=1000, value=1500)
displacement = st.number_input("What is the engine displacement of your car (in cc)?", min_value=500, value=500)
turning_radius = st.number_input("What is the turning radius of your car (in meters)?", min_value=4.5, value=4.5)

# Binary features
is_front_fog_lights = 1 if st.radio("Does your car have front fog lights?", ("Yes", "No")) == "Yes" else 0
is_rear_window_wiper = 1 if st.radio("Does your car have a rear window wiper?", ("Yes", "No")) == "Yes" else 0
is_rear_window_washer = 1 if st.radio("Does your car have a rear window washer?", ("Yes", "No")) == "Yes" else 0
is_rear_window_defogger = 1 if st.radio("Does your car have a rear window defogger?", ("Yes", "No")) == "Yes" else 0
is_brake_assist = 1 if st.radio("Does your car have brake assist?", ("Yes", "No")) == "Yes" else 0
is_power_door_locks = 1 if st.radio("Does your car have power door locks?", ("Yes", "No")) == "Yes" else 0
is_central_locking = 1 if st.radio("Does your car have central locking?", ("Yes", "No")) == "Yes" else 0
is_power_steering = 1 if st.radio("Does your car have power steering?", ("Yes", "No")) == "Yes" else 0
is_driver_seat_height_adjustable = 1 if st.radio("Is the driver’s seat height adjustable?", ("Yes", "No")) == "Yes" else 0
is_day_night_rear_view_mirror = 1 if st.radio("Does your car have a day-night rear view mirror?", ("Yes", "No")) == "Yes" else 0
is_ecw = 1 if st.radio("Does your car have electronic control windows?", ("Yes", "No")) == "Yes" else 0
is_speed_alert = 1 if st.radio("Does your car have a speed alert system?", ("Yes", "No")) == "Yes" else 0
is_esc = 1 if st.radio("Does your car have electronic stability control?", ("Yes", "No")) == "Yes" else 0
is_adjustable_steering = 1 if st.radio("Is the steering wheel adjustable?", ("Yes", "No")) == "Yes" else 0
is_tpms = 1 if st.radio("Does your car have a tire pressure monitoring system?", ("Yes", "No")) == "Yes" else 0
is_parking_sensors = 1 if st.radio("Does your car have parking sensors?", ("Yes", "No")) == "Yes" else 0
is_parking_camera = 1 if st.radio("Does your car have a parking camera?", ("Yes", "No")) == "Yes" else 0

# Create input DataFrame
input_data = pd.DataFrame({
    'policy_tenure': [policy_tenure],
    'age_of_car': [age_of_car],
    'age_of_policyholder': [age_of_policyholder],
    'length': [length],
    'width': [width],
    'height': [height],
    'ncap_rating': [ncap_rating],
    'segment': [segment],
    'fuel_type': [fuel_type],
    'max_torque': [max_torque],
    'max_power': [max_power],
    'airbags': [airbags],
    'rear_brakes_type': [rear_brakes_type],
    'cylinder': [cylinder],
    'transmission_type': [transmission_type],
    'gear_box': [gear_box],
    'steering_type': [steering_type],
    'gross_weight': [gross_weight],
    'displacement': [displacement],
    'turning_radius': [turning_radius],
    'is_front_fog_lights': [is_front_fog_lights],
    'is_rear_window_wiper': [is_rear_window_wiper],
    'is_rear_window_washer': [is_rear_window_washer],
    'is_rear_window_defogger': [is_rear_window_defogger],
    'is_brake_assist': [is_brake_assist],
    'is_power_door_locks': [is_power_door_locks],
    'is_central_locking': [is_central_locking],
    'is_power_steering': [is_power_steering],
    'is_driver_seat_height_adjustable': [is_driver_seat_height_adjustable],
    'is_day_night_rear_view_mirror': [is_day_night_rear_view_mirror],
    'is_ecw': [is_ecw],
    'is_speed_alert': [is_speed_alert],
    'is_esc': [is_esc],
    'is_adjustable_steering': [is_adjustable_steering],
    'is_tpms': [is_tpms],
    'is_parking_sensors': [is_parking_sensors],
    'is_parking_camera': [is_parking_camera]
})

# One-hot encode input data
input_data_encoded = pd.get_dummies(input_data)

# Reindex input data to match the feature columns used during training
input_data_encoded = input_data_encoded.reindex(columns=feature_columns, fill_value=0)

# Scale features
input_data_scaled = scaler.transform(input_data_encoded)

# Predict using the model
prediction = model.predict(input_data_scaled)
prediction_proba = model.predict_proba(input_data_scaled)


# Prediction button
if st.button('Predict'):
    # Predict probabilities
    prediction_proba = model.predict_proba(input_data_scaled)
    
    # Adjust the threshold
    threshold = 0.51  # Example threshold; you may adjust based on validation
    prediction = (prediction_proba[:, 1] >= threshold).astype(int)

    # Output prediction
    st.subheader('Prediction')
    st.write(f'Predicted Class: {"Claim" if prediction[0] == 1 else "No Claim"}')
    st.write(f'Probability: {prediction_proba[0][1]:.2f}')
