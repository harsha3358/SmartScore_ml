from fastapi import FastAPI
import joblib
import numpy as np
from app.schemas import StudentInput

app = FastAPI(title="SmartScore AI")

model = joblib.load("model/model.pkl")

@app.get("/")
def home():
    return {"message": "SmartScore AI is running"}

@app.post("/predict")
def predict(data: StudentInput):
    input_data = np.array([[ 
        data.study_hours,
        data.sleep_hours,
        data.screen_time,
        data.attendance,
        data.practice_tests
    ]])

    prediction = model.predict(input_data)[0]

    return {"predicted_score": round(prediction, 2)}