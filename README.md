Policyholder Claim Prediction
Dataset Overview
The dataset used for this project contains detailed information on policyholders, including:

Policy Tenure
Age of the Car
Age of the Owner
City Population Density
Car Make and Model
Engine Power
Engine Type
The target variable, is_claim, indicates whether a policyholder is likely to file a claim within the next six months.

Data Cleaning
Initial Size: 61,521 records, 44 features.
After Cleaning: 57,371 records, 43 features (duplicates and irrelevant data removed).
Analysis Focus
Target Variable: The analysis focused on is_claim to understand factors influencing the likelihood of a claim.
Distribution Analysis: Explored the distribution of is_claim and its relationship with key features.
Machine Learning Process
Encoding: Categorical features were transformed using one-hot encoding with pd.get_dummies().
Imbalance Handling: Applied SMOTEENN to balance the classes and improve model learning.
Scaling: Continuous features were scaled using StandardScaler.
Modeling: Built classification models to predict is_claim without hyperparameter tuning or cross-validation.
Conclusion
The developed predictive model helps identify policyholders likely to file claims, supporting effective decision-making in risk management.
