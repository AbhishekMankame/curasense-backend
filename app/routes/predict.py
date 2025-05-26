from fastapi import APIRouter
from pydantic import BaseModel, validator
from typing import List
from app import predict # import the prediction logic module

router = APIRouter()

class DiseasePredictionRequest(BaseModel):
    symptoms: List[str]

    @validator("symptoms")
    def validate_symptoms(cls, v):
        if not v or not isinstance(v, list):
            raise ValueError("Symptoms must be a non-empty list of strings.")
        if not all(isinstance(symptom, str) and symptom.strip() for symptom in v):
            raise ValueError("Each symptom must be a non-empty-string.")
        return v