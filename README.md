# 🏦 Bank Customer Churn Prediction

A complete data science project that predicts whether a bank customer is likely to churn. This project uses supervised machine learning models and explains churn drivers using SHAP. It also includes a deployable Streamlit dashboard.

---

## 📁 Project Structure

<pre lang="nohighlight"><code>```bash bank-churn-project/ ├── data/ │ └── BankCustomerChurnPrediction.csv # Raw dataset from Kaggle ├── notebooks/ │ ├── 01_eda.ipynb # Data analysis and visualization │ ├── xgb_model.pkl # Trained XGBoost model │ └── scaler.pkl # Scaler used for input features ├── dashboard/ │ └── app.py # Streamlit app for churn prediction ├── Business Recommendations & Reporting.txt # Insights and strategy document └── README.md # Project overview ```</code></pre>

---

## 🎯 Project Objective

The goal is to help a bank **predict customer churn** and take **proactive retention steps**. Churn prediction enables the bank to:
- Reduce revenue loss
- Target at-risk customers
- Improve customer satisfaction

---

## 🧠 Problem Statement

Given customer data (e.g., age, credit score, account balance, products used), predict whether the customer will **leave the bank (`churn = 1`)** or **stay (`churn = 0`)**.

---

## 📊 Dataset

**Source:** [Kaggle - Bank Customer Churn Dataset](https://www.kaggle.com/datasets/gauravtopre/bank-customer-churn-dataset)

- Records: 10,000 customers
- Features:
  - `credit_score`, `gender`, `age`, `balance`, `tenure`, `products_number`, `country`, `credit_card`, `active_member`, `estimated_salary`, and `churn` (target)

---

## 🛠️ Technologies Used

- **Python**
- **Pandas, NumPy** — Data handling
- **Matplotlib, Seaborn** — Visualization
- **Scikit-learn** — Preprocessing & ML models
- **XGBoost** — Advanced classifier
- **SHAP** — Model interpretability
- **Streamlit** — Dashboard deployment

---

## 📈 ML Models Trained

| Model                | Evaluation Metric (F1 / ROC AUC) |
|---------------------|-----------------------------------|
| Logistic Regression | ✅ Baseline                       |
| Random Forest       | ✅ Good performance               |
| **XGBoost**         | ⭐ Best (used in final dashboard) |

---

## 🧪 Project Steps

### ✅ Step 1: Define Problem
- Business objective and churn definition

### ✅ Step 2: Load & Explore Dataset
- Checked nulls, duplicates, distribution

### ✅ Step 3: Clean & Preprocess
- Encoded categorical features, scaled numerical ones

### ✅ Step 4: EDA
- Visualized churn by age, gender, country, balance, activity

### ✅ Step 5: Train Models
- Compared multiple classification models

### ✅ Step 6: Interpret Models
- Used SHAP to understand why churn happens

### ✅ Step 7: Business Recommendations
- Created a report for management with actions

### ✅ Step 8: Streamlit Dashboard
- Predicts churn risk based on customer input

---

## 🖥️ Streamlit Dashboard

The `dashboard/app.py` allows users to interactively input customer details and predict churn in real time.

### ▶️ Run the app:
``` bash
streamlit run dashboard/app.py
```
---

## 📄 Business Recommendations (Summary)
Older, inactive, and low-product customers are most likely to churn.
Germany shows higher churn rates.
Suggest incentives, loyalty programs, and regional engagement.
→ Full report in: Business Recommendations & Reporting.txt

---

### 🔍 SHAP Feature Importance (Sample)
Top contributors to churn:
- Age ↑
- Inactivity
- High balance
- Country (e.g., Germany)
- Few products

---

## 🚀 Future Enhancements
Add database or cloud support for live data
Deploy to Streamlit Cloud or HuggingFace Spaces
Track customer LTV for targeted marketing

---

## 📜 License
This project is open-source and available under the MIT License.
