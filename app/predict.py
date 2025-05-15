from fastapi import APIRouter
from pydantic import BaseModel, validator
from typing import List

# 🧾 First: define the request model
class DiseasePredictionRequest(BaseModel):
    symptoms: List[str]  # List of symptoms

    @validator('symptoms')
    def validate_symptoms(cls, v):
        if not v or not isinstance(v, list) or len(v) == 0:
            raise ValueError("Symptoms list cannot be empty.")
        if not all(isinstance(symptom, str) and symptom.strip() for symptom in v):
            raise ValueError("All symptoms must be non-empty strings.")
        return v

# 🤖 Then: define the prediction function
def predict_disease(request: DiseasePredictionRequest):
    symptoms = request.symptoms
    return {
        "predicted_disease": "Placeholder Disease",
        "symptoms": symptoms,
        "message": "Prediction based on symptoms received"
    }
