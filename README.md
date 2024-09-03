Policyholder Claim Prediction

The dataset provides detailed information about policyholders, including policy tenure, age of the car, age of the owner, city population density, car make and model, engine power, and engine type. The target variable, is_claim, indicates whether a policyholder is likely to file a claim within the next six months.

The initial dataset size was 61,521 records with 44 features. After cleaning, the dataset was reduced to 57,371 records with 43 features (duplicates and irrelevant data removed).

The analysis focused on the is_claim variable to understand factors influencing the likelihood of a claim. Distribution analysis examined is_claim and its relationship with key features.

The machine learning process involved encoding categorical features with pd.get_dummies(), handling class imbalance using SMOTEENN, scaling continuous features with StandardScaler, and building classification models to predict is_claim without hyperparameter tuning or cross-validation.

The developed predictive model helps identify policyholders likely to file claims, supporting effective decision-making in risk management.
