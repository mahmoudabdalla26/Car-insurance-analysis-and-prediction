# Import necessary libraries
import streamlit as st
# Import custom modules for data analysis and visualization from 'MEDA.py'
from MEDA import load_data, clean_data, create_pie_chart, create_histograms, create_histogram_subplots, correlation_heatmap

# Constants
FILE_PATH = r"car_insurance/Sourse/modified_train_subset.csv"
NUMERICAL_COLUMNS = ['policy_tenure', 'age_of_car', 'age_of_policyholder', 'population_density', 'make',
                     'airbags', 'displacement', 'cylinder', 'gear_box', 'length', 'width', 'height',
                     'gross_weight', 'ncap_rating', 'turning_radius']
SUBPLOT_COLUMNS = ['area_cluster', 'population_density', 'model', 'fuel_type', 'airbags', 'displacement',
                   'cylinder', 'transmission_type', 'gear_box', 'steering_type', 'turning_radius']
IS_COLUMNS = ['is_esc', 'is_adjustable_steering', 'is_tpms', 'is_parking_sensors', 'is_parking_camera',
              'is_front_fog_lights', 'is_rear_window_wiper', 'is_rear_window_washer', 'is_rear_window_defogger',
              'is_brake_assist', 'is_power_door_locks', 'is_central_locking', 'is_power_steering',
              'is_driver_seat_height_adjustable', 'is_day_night_rear_view_mirror', 'is_ecw', 'is_speed_alert']

# Load and clean the data
df = load_data(FILE_PATH)  
df = clean_data(df)        

# Title of the app
st.title('Model Evaluation and Data Analysis Dashboard')

# Data Overview
st.header('Data Overview')
st.write(df.head())

# Pie Chart for Distribution of 'is_claim'
st.header('Claims Distribution')
is_claim_count = df['is_claim'].value_counts()
st.plotly_chart(create_pie_chart(df, 'is_claim'))

# Display insights
st.subheader("Key Insights")
total_records = is_claim_count.sum()
no_claims_percentage = is_claim_count[0] / total_records * 100
claims_percentage = is_claim_count[1] / total_records * 100

st.write(f"- **No Claims (0):** {is_claim_count[0]} records (approximately {no_claims_percentage:.2f}%)")
st.write(f"- **Claims (1):** {is_claim_count[1]} records (approximately {claims_percentage:.2f}%)")
st.write(f"- **Imbalance:** The dataset is highly imbalanced, with a significantly higher proportion of records indicating no claims compared to those indicating claims.")
st.write(f"- **Impact on Analysis:** This imbalance may affect the performance of predictive models, making it important to consider techniques for handling class imbalance, such as resampling or using algorithms designed to address imbalanced data.")

# Histograms for numerical columns
st.header('Histograms of Numerical Columns')
st.plotly_chart(create_histograms(df, NUMERICAL_COLUMNS))

# Insights
st.header("Policy Activation Duration")
st.write("Most people (7,000) have had their policy active for at least 3 years.")
st.write("The majority of people opt for insurance immediately when they purchase a car.")

st.header("Age of Policyholders")
st.write("Most policyholders are between 30 and 40 years old.")

st.header("Car Make Preferences")
st.write("Most people prefer cars from 'Make 1', followed by 'Make 3'.")
st.write("The least preferred makes are 'Make 2', 'Make 4', and 'Make 5'.")

st.header("Airbags in Cars")
st.write("The number of airbags in most cars is 5.")
st.write("Most cars have 2 airbags (40,000+), followed by 6 airbags (approximately 17,000).")
st.write("The 1 airbag option is present in almost 1,000 cars, while no cars have 3, 4, or 5 airbags.")

st.header("NCAP Rating of Cars")
st.write("Most cars have an NCAP rating of 2 (20,000+), followed by a rating of 0 (approximately 19,000).")
st.write("Cars with ratings of 4 and 5 are considered the safest (2,500 each).")

# Histograms for columns with subplots compared to 'is_claim'
st.header('Histograms of Columns with Subplots Compared to "is_claim"')
fig = create_histogram_subplots(df, SUBPLOT_COLUMNS)
st.plotly_chart(fig)

# Insights
st.header('High Claim Density in Area C8')
st.write('The highest number of claims, approximately 1000, comes from area C8.')

st.header('High Claims Among Specific Car Models (M1, M4, M6)')
st.write('Owners of models M1, M4, and M6 have the highest claims, with about 1000 claims each.')

st.header('Zero Claims Without Speed Alert System')
st.write('There are zero claims where the speed alert system isn\'t present in the car.')

# Histogram for columns starting with 'is_' based on 'is_claim'
st.header('Histogram of Columns with "is_" based on "is_claim"')
fig = create_histogram_subplots(df, IS_COLUMNS)
st.plotly_chart(fig)

# Correlation Heatmap for bottom features with 'is_claim'
st.header('Correlation Heatmap of Bottom Features with "is_claim"')
st.plotly_chart(correlation_heatmap(df, 'is_claim', 10))
