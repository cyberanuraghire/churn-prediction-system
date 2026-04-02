import streamlit as st
import requests

st.title("🏦 Customer Churn Prediction")

# Inputs
credit = st.number_input("Credit Score", 300, 900, 650)
age = st.number_input("Age", 18, 100, 35)
tenure = st.number_input("Tenure", 0, 10, 5)
balance = st.number_input("Balance", 0.0, 200000.0, 50000.0)
products = st.number_input("Number of Products", 1, 4, 2)
card = st.selectbox("Has Credit Card", [0, 1])
active = st.selectbox("Is Active Member", [0, 1])
salary = st.number_input("Estimated Salary", 0.0, 200000.0, 60000.0)

geo_germany = st.selectbox("Germany", [0, 1])
geo_spain = st.selectbox("Spain", [0, 1])
gender = st.selectbox("Male", [0, 1])

if st.button("Predict"):

    data = {
        "CreditScore": credit,
        "Age": age,
        "Tenure": tenure,
        "Balance": balance,
        "NumOfProducts": products,
        "HasCrCard": card,
        "IsActiveMember": active,
        "EstimatedSalary": salary,
        "Geography_Germany": geo_germany,
        "Geography_Spain": geo_spain,
        "Gender_Male": gender
    }

    response = requests.post("http://127.0.0.1:8000/predict", json=data)

    result = response.json()

    if result["prediction"] == 1:
        st.error("⚠ Customer likely to churn")
    else:
        st.success("✅ Customer likely to stay")

    st.write("Probability:", result["probability"])
    st.write("Risk Level:", result["risk_level"])