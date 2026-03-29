from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import numpy as np

model = joblib.load('cancer_model.pkl')
scaler = joblib.load('scaler.pkl')

app = FastAPI(title="SheCare AI API")

# ✅ Autoriser le frontend React
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class PatientData(BaseModel):
    features: list[float]

@app.get("/")
def home():
    return {"message": "SheCare AI est en ligne "}

@app.post("/predict")
def predict(data: PatientData):
    X = np.array(data.features).reshape(1, -1)
    X_scaled = scaler.transform(X)
    proba = model.predict(X_scaled)[0]
    resultat = "Bénin ✅" if proba > 0.5 else "Malin ⚠️"
    return {
        "resultat": resultat,
        "probabilite": round(float(proba), 4),
        "message": "Consulte un médecin pour confirmation"
    }