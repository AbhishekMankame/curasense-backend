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
    input_symptoms = set(symptom.lower() for symptom in request.symptoms)

    best_match = None
    highest_match_count = 0