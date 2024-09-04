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
    st.image("https://cdnl.iconscout.com/lottie/premium/preview-watermark/accident-insurance-animation-download-in-lottie-json-gif-static-svg-file-formats--car-coverage-auto-claim-collision-crash-pack-services-animations-7487779.mp4", width=500)
st.markdown('''
<center> <h10>
            Done by : Mahmoud Abdelhamid <br>
            Supervised by : Epsilon AI <br>
            
            ''',unsafe_allow_html=True)
