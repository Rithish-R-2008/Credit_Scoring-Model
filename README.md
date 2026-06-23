# 💳 Credit Scoring Model for Predicting Creditworthiness

An end-to-end Machine Learning project that predicts whether a loan applicant is a **Good Credit Risk** or a **Bad Credit Risk** based on their financial history and profile information.

The application leverages a **Random Forest Classifier** trained on a synthetic dataset and provides real-time predictions through an interactive **Streamlit** web interface.

📌 Project Overview

Financial institutions rely on credit scoring systems to assess the likelihood of borrowers repaying loans. This project demonstrates how Machine Learning can automate that process by analyzing key financial indicators and classifying applicants according to their creditworthiness.

🚀 Features

* **Automated Dataset Generation**

  * Generates synthetic borrower records for training and testing.

* **Machine Learning Pipeline**

  * Data preprocessing, model training, evaluation, and model persistence.

* **Random Forest Classifier**

  * Robust ensemble learning algorithm for accurate credit risk prediction.

* **Interactive Streamlit Dashboard**

  * User-friendly interface for entering borrower details and receiving instant predictions.

* **Comprehensive Model Evaluation**

  * Accuracy
  * Precision
  * Recall
  * F1-Score
  * ROC-AUC Score

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Joblib
* Streamlit
* Matplotlib
* Seaborn

---

## 📂 Project Structure

```text
Credit_Scoring_Model/
│
├── generate_dataset.py      # Generates synthetic credit data
├── train_model.py           # Trains and evaluates the ML model
├── app.py                   # Streamlit web application
├── credit_data.csv          # Generated dataset
├── credit_model.pkl         # Trained model
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
cd YOUR_REPOSITORY_NAME
```

### 2. Create a Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

### Step 1: Generate the Dataset

```bash
python generate_dataset.py
```

This creates a synthetic dataset containing borrower information.

---

### Step 2: Train the Model

```bash
python train_model.py
```

This script:

* Loads the dataset
* Trains the Random Forest Classifier
* Evaluates model performance
* Saves the trained model for deployment

---

### Step 3: Launch the Streamlit Application

```bash
streamlit run app.py
```

The application will open in your browser, allowing you to enter applicant details and obtain instant credit risk predictions.

📊 Model Evaluation Metrics

The model is evaluated using the following performance metrics:

| Metric    | Description                                |
| --------- | ------------------------------------------ |
| Accuracy  | Overall prediction correctness             |
| Precision | Accuracy of positive credit predictions    |
| Recall    | Ability to identify good credit applicants |
| F1-Score  | Balance between Precision and Recall       |
| ROC-AUC   | Overall classification performance         |

📈 Sample Workflow

1. Generate borrower dataset.
2. Train the Random Forest model.
3. Evaluate model performance.
4. Save the trained model.
5. Launch Streamlit dashboard.
6. Enter applicant details.
7. Receive real-time creditworthiness prediction.

🔮 Future Enhancements

* [ ] Integrate real-world datasets such as the German Credit Dataset.
* [ ] Implement advanced algorithms like XGBoost and LightGBM.
* [ ] Add SHAP-based model explainability.
* [ ] Deploy the application on AWS, Azure, or Render.
* [ ] Develop REST APIs for enterprise integration.
* [ ] Enable batch prediction functionality.

🎯 Learning Outcomes

This project demonstrates:

* Data Generation & Preprocessing
* Feature Engineering
* Classification Algorithms
* Model Evaluation Techniques
* Model Deployment with Streamlit
* End-to-End Machine Learning Workflow

📜 License

This project is intended for educational and portfolio purposes. Feel free to modify and extend it for your own learning and development.

---

### ⭐ If you found this project useful, consider giving the repository a star!
