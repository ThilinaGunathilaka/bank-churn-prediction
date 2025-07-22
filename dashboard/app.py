import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Load your trained model and scaler
model = joblib.load("xgb_model.pkl")  # Save your model as shown below
scaler = joblib.load("scaler.pkl")    # Save your scaler too

# Streamlit App
st.title("💳 Bank Customer Churn Prediction App")
st.write("Enter customer details to predict churn risk.")

# Input fields
credit_score = st.slider("Credit Score", 300, 900, 600)
age = st.slider("Age", 18, 100, 40)
tenure = st.slider("Tenure (Years at Bank)", 0, 10, 5)
balance = st.number_input("Account Balance", value=10000.00)
products_number = st.selectbox("Number of Products", [1, 2, 3, 4])
credit_card = st.radio("Has Credit Card?", ["Yes", "No"])
active_member = st.radio("Active Member?", ["Yes", "No"])
estimated_salary = st.number_input("Estimated Salary", value=50000.00)
gender = st.radio("Gender", ["Male", "Female"])
country = st.selectbox("Country", ["France", "Germany", "Spain"])

# Preprocess input
gender = 1 if gender == "Male" else 0
credit_card = 1 if credit_card == "Yes" else 0
active_member = 1 if active_member == "Yes" else 0

# One-hot encode country
country_Germany = 1 if country == "Germany" else 0
country_Spain = 1 if country == "Spain" else 0

# Create input vector
input_data = np.array([[credit_score, gender, age, tenure, balance, products_number,
                        credit_card, active_member, estimated_salary,
                        country_Germany, country_Spain]])

# Scale input
input_scaled = scaler.transform(input_data)

# Predict
if st.button("Predict"):
    prediction = model.predict(input_scaled)
    if prediction[0] == 1:
        st.error("⚠️ This customer is likely to churn.")
    else:
        st.success("✅ This customer is likely to stay.")
