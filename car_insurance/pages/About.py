import streamlit as st

# Title of the App
st.title("Policyholder Claim Prediction")

# Dataset Overview Section
st.header("Dataset Overview")
st.write("""
The dataset contains information on policyholders, including features like policy tenure, age of the car, 
age of the owner, city population density, car make and model, engine power, and engine type. 
The target variable, `is_claim`, indicates whether a policyholder is likely to file a claim within the next six months.
""")

# Data Cleaning Section
st.header("Data Cleaning")
st.write("""
- **Initial Size**: 61,521 records, 44 features.
- **After Cleaning**: 57,371 records, 43 features (after removing duplicates and irrelevant data).
""")

# Analysis Focus Section
st.header("Analysis Focus")
st.write("""
- **Target Variable**: The analysis primarily focused on `is_claim` to understand factors influencing the likelihood of a claim.
- **Distribution Analysis**: Examined the distribution of `is_claim` and its relationship with key features.
""")

# Machine Learning Process Section
st.header("Machine Learning Process")
st.write("""
- **Encoding**: Categorical features were transformed using one-hot encoding with `get_dummies()`.
- **Imbalance Handling**: Used SMOTEENN to balance the classes, ensuring effective model learning.
- **Scaling**: Continuous features were scaled using `StandardScaler`.
- **Modeling**: Built classification models to predict `is_claim` without hyperparameter tuning or cross-validation.
""")

# Conclusion Section
st.header("Conclusion")
st.write("""
The process led to the development of a predictive model that helps identify policyholders likely to file claims, 
supporting effective decision-making in risk management.
""")
