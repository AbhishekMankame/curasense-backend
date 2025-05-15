from fastapi import FastAPI
from dotenv import load_dotenv
from app.predict import predict_disease, DiseasePredictionRequest # Import the whole predict module
import os

# Load environment variables
load_dotenv()

# Initialize the FASTAPI app
app = FastAPI()

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Hello, Welcome to CuraSense!"}

# Include the predict router
@app.post("/predict_disease")
def predict_symptoms(request: DiseasePredictionRequest):
    return predict_disease(request)