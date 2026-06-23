import pandas as pd
import numpy as np
import os

np.random.seed(42)
n = 1000

data = pd.DataFrame({
    'Age': np.random.randint(21, 60, n),
    'Income': np.random.randint(20000, 150000, n),
    'LoanAmount': np.random.randint(5000, 50000, n),
    'CreditScore': np.random.randint(300, 850, n),
    'Debt': np.random.randint(0, 100000, n),
    'EmploymentYears': np.random.randint(0, 30, n),
    'MissedPayments': np.random.randint(0, 10, n),
    'Savings': np.random.randint(1000, 50000, n)
})

# Logic to determine creditworthiness
data['Creditworthy'] = (
    (data['CreditScore'] > 650) &
    (data['Debt'] < 50000) &
    (data['MissedPayments'] < 3)
).astype(int)

# Ensure the 'data' directory exists before saving
os.makedirs("data", exist_ok=True)
data.to_csv("data/credit_data.csv", index=False)

print("Dataset Created Successfully in data/credit_data.csv")