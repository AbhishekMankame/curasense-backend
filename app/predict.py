from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

# Define a request model for disease prediction
class DiseasePredictionRequest(BaseModel):
    symptoms: List[str] # List of symptoms as strings