from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import joblib

# Load artifacts
model = joblib.load('../model/churn_model.pkl')
scaler = joblib.load('../model/scaler.pkl')
features = joblib.load('../model/features.pkl')

app = FastAPI(title="Churn Prediction API")

# Input schema
class CustomerData(BaseModel):
    CreditScore: float
    Age: float
    Tenure: float
    Balance: float
    NumOfProducts: float
    HasCrCard: float
    IsActiveMember: float
    EstimatedSalary: float
    Geography_Germany: float
    Geography_Spain: float
    Gender_Male: float

@app.get("/")
def home():
    return {"message": "API Running"}
@app.post("/predict")
def predict(data: CustomerData):
    try:
        input_dict = data.dict()

# 🔥 ALL FEATURE ENGINEERING (COMPLETE)

        input_dict['BalanceSalaryRatio'] = input_dict['Balance'] / (input_dict['EstimatedSalary'] + 1)
        input_dict['TenureAgeRatio'] = input_dict['Tenure'] / (input_dict['Age'] + 1)

        input_dict['HasBalance'] = 1 if input_dict['Balance'] > 0 else 0

        input_dict['IsActive_by_Balance'] = input_dict['IsActiveMember'] * input_dict['Balance']

# CreditScoreBucket (same as training)
        import numpy as np
        input_dict['CreditScoreBucket'] = int(np.digitize(input_dict['CreditScore'], bins=[400, 500, 600, 700, 800]))

# 🔥 ADD THIS (your missing one)
        salary_median = 60000   # approx (or compute from training if you saved)
        input_dict['IsHighIncome'] = 1 if input_dict['EstimatedSalary'] > salary_median else 0
        input_list = [input_dict[f] for f in features]
        input_array = np.array([input_list])

        input_scaled = scaler.transform(input_array)

        prob = model.predict_proba(input_scaled)[0][1]
        pred = int(prob > 0.5)
        # 🔥 ADD THIS
        if prob < 0.3:
            risk = "Low"
        elif prob < 0.6:
            risk = "Medium"
        else:
            risk = "High"

        return {
    "prediction": pred,
    "probability": float(prob),
    "risk_level": risk   # ✅ added
}

    except Exception as e:
        return {"error": str(e)}