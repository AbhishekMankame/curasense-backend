from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

# Sample rule-based database
disease_symptom_map = {
    "Flu" : {"fever", "cough", "sore throat", "fatigue"},
    "Common Cold" : {"snezzing", "stuffy nose", "cough"},
    "COVID-19" : {"fever", "cough", "loss of taste", "shortness of breath"},
    "Malaria" : {"fever", "chills", "sweating", "headache"},
    "Dengue" : {"fever", "rash", "joint pain", "nausea"}
}

# Define a request model for disease prediction
class DiseasePredictionRequest(BaseModel):
    symptoms: List[str] # List of symptoms as strings

@router.post("/predict_disease")
def predict_disease(request: DiseasePredictionRequest):
    symptoms = request.symptoms
    # For now, we are returning a placeholder prediction
    return {
        "predicted_disease": "Placeholder Disease",
        "symptoms": symptoms,
        "message": "Prediction based on symptoms received"
    }