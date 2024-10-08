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

col1, col2, col3 = st.columns([1,3,1])

with col2:
    st.image("https://static.pbcdn.in/cdn/images/articles/car/importance-and-benefits-of-comprehensive-car-insurance-policy.jpg", width=500)
st.markdown('''
<center> <h10>
            Done by : Mahmoud Abdelhamid <br>
            Supervised by : Epsilon AI <br>
            
            ''',unsafe_allow_html=True)
