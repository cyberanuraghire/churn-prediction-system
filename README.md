Title
Customer Churn Prediction System (BFSI Domain)
📌 Description

End-to-end machine learning system to predict customer churn using XGBoost, deployed via FastAPI and Streamlit for real-time inference.

📌 Features
Customer churn prediction (Stay / Leave)
Probability in percentage
Risk classification (Low / Medium / High)
Interactive UI dashboard
REST API backend
📌 Tech Stack
Python
Scikit-learn
XGBoost
FastAPI
Streamlit
📌 Workflow
Data preprocessing & EDA
Feature engineering
Model training (XGBoost)
Hyperparameter tuning
Model deployment (FastAPI)
UI integration (Streamlit)
📌 Run Locally
git clone <repo>
cd churn-system

# backend
cd backend
uvicorn main:app --reload

# frontend
cd ../frontend
streamlit run app.py