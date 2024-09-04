# Import necessary libraries
import numpy as np 
import pandas as pd 
import streamlit as st 
from PIL import Image 

# Title 
st.markdown(" <center>  <h1>  Car Insurance Claim Prediction Analysis </h1> </font> </center> </h1> ",
            unsafe_allow_html=True)

# About the project
st.markdown(''' <center>  <h6>
    This app is created to analyze and predict the likelihood of policyholders filing a car insurance claim. </center> </h6> ''', 
            unsafe_allow_html=True)

# Open the image file
image = Image.open(r"car_insurance/Sourse/WhatsApp Image 2024-09-03 at 12.44.33_9e1eda42.jpg")

# Define desired width and height
desired_width = 250
desired_height = 200

# Resize the image
resized_image = image.resize((desired_width, desired_height))

# Display the resized image using Streamlit
st.image(resized_image, caption='Car Insurance Claim Prediction', use_column_width=True)
