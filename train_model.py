import pandas as pd
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score

# Load data
data = pd.read_csv("data/credit_data.csv")

X = data.drop("Creditworthy", axis=1)
y = data["Creditworthy"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print("Accuracy:", accuracy)
print("\nClassification Report:\n", classification_report(y_test, predictions))
print("ROC-AUC Score:", roc_auc_score(y_test, predictions))

# Ensure the 'models' directory exists before saving
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/credit_model.pkl")

print("Model Saved Successfully in models/credit_model.pkl")