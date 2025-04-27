from fastapi import FastAPI
from dotenv import load_dotenv
from app.predict import predict_disease, DiseasePredictionRequest
import os
# Load environment variables
load_dotenv()

# Now you can access like
# secret_key = os.getenv("SECRET_KEY")
# print(secret_key)

# Initialize the FASTAPI app
app = FastAPI()

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Hello, Welcome to CuraSense!"}

# Disease prediction endpoint
@app.post("/predict_disease")
def predict_disease(request: DiseasePredictionRequest):
   # return predict_disease(request)
     symptoms = request.symptoms
    # For now, we are returning a placeholder prediction
    # In the future, this will be replaced by machine learning model
     return {
       "predicted_disease": "Placeholder Disease",
        "symptoms": symptoms,
        "message": "Prediction based on symptoms received"
     }