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

    for disease, symptoms in disease_symptom_map.items():
        matched = len(input_symptoms & {s.lower() for s in symptoms})
        if matched > highest_match_count:
            highest_match_count = matched
            best_match = disease

    return {
        "predicted_disease" : best_match or "Unknown",
        "matched_symptom_count" : highest_match_count,
        "symptoms" : request.symptoms,
        "message" : "Prediction based on symptom matching"
    }