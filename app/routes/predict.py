import joblib
from fastapi import APIRouter
from pydantic import BaseModel, validator
from typing import List

router = APIRouter()

# Load model and encoders once when this module loads
clf = joblib.load("model/disease_predictor.pkl")
mlb = joblib.load("model/symptom_encoder.pkl")
le = joblib.load("model/disease_label_encoder.pkl")

class DiseasePredictionRequest(BaseModel):
    symptoms: List[str]

    @validator("symptoms")
    def validate_symptoms(cls, v):
        if not v or not isinstance(v, list):
            raise ValueError("Symptoms must be a non-empty list of strings.")
        if not all(isinstance(symptom, str) and symptom.strip() for symptom in v):
            raise ValueError("Each symptom must be a non-empty string.")
        return v

@router.post("/predict_disease")
def predict_disease(request: DiseasePredictionRequest):
    symptoms = request.symptoms
    # Encode symptoms into multi-hot vector
    symptom_vector = mlb.transform([symptoms])
    # Predict encoded disease label
    pred_label_encoded = clf.predict(symptom_vector)[0]
    # Decode label to disease name
    predicted_disease = le.inverse_transform([pred_label_encoded])[0]

    return {
        "predicted_disease": predicted_disease,
        "symptoms": symptoms,
        "message": "Prediction based on symptoms received"
    }
