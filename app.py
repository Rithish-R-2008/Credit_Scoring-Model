import streamlit as st
import joblib
import pandas as pd

# Load the trained model
model = joblib.load("models/credit_model.pkl")

st.title("Credit Scoring Prediction System")
st.write("Enter applicant details to predict creditworthiness.")

# Layout with two columns for clean UI
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", 18, 80, value=30)
    income = st.number_input("Annual Income ($)", min_value=0, value=50000)
    loan_amount = st.number_input("Requested Loan Amount ($)", min_value=0, value=15000)
    credit_score = st.number_input("Credit Score", 300, 850, value=700)

with col2:
    debt = st.number_input("Total Debt ($)", min_value=0, value=10000)
    employment = st.number_input("Years of Employment", 0, 50, value=5)
    missed = st.number_input("Number of Missed Payments", 0, 20, value=0)
    savings = st.number_input("Total Savings ($)", min_value=0, value=5000)

if st.button("Predict Creditworthiness", use_container_width=True):
    # Match the column ordering of the training features exactly
    sample = pd.DataFrame({
        'Age': [age],
        'Income': [income],
        'LoanAmount': [loan_amount],
        'CreditScore': [credit_score],
        'Debt': [debt],
        'EmploymentYears': [employment],
        'MissedPayments': [missed],
        'Savings': [savings]
    })

    prediction = model.predict(sample)

    st.markdown("---")
    if prediction[0] == 1:
        st.success("🎉 **Result: Good Credit Risk** (Loan Recommended)")
    else:
        st.error("⚠️ **Result: Bad Credit Risk** (High Risk of Default)")