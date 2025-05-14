from fastapi import APIRouter
from pydantic import BaseModel, validator
from typing import List

# Define a request model for disease prediction
class DiseasePredictionRequest(BaseModel):
    symptoms: List[str] # List of symptoms

    @validator('symptoms')
    def validate_symptoms(cls, v):
        if not v or not isinstance(v, list) or len(v) == 0:
            raise ValueError("Symptom list cannot be empty.")
        if not all(isinstance(symptom, str) and symptom.strip() for symptom in v):
            raise ValueError("All symptoms must me non-empty strings.")
        return v