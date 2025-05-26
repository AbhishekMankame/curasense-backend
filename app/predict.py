from typing import List
import joblib
import os

# Load the trained model and encoders
MODEL_DIR = "model"
MODEL_FILE = os.path.join(MODEL_DIR, "disease_predictor.pkl")
SYMPTOM_ENCODER_FILE = os.path.join(MODEL_DIR, "symptom_encoder.pkl")
DISEASE_LABEL_ENCODER_FILE = os.path.join(MODEL_DIR, "disease_label_encoder.pkl")

clf = joblib.load(MODEL_FILE)
mlb = joblib.load(SYMPTOM_ENCODER_FILE)
le = joblib.load(DISEASE_LABEL_ENCODER_FILE)

def run_prediction(symptoms: List[str]) -> str:
    """
    Predicts the disease based on input symptoms using the trained RandomForest model.
    
    Args:
        symptoms (List[str]): List of symptoms as strings.
    
    Returns:
        str: Predicted disease.
    """
    # Preprocess the symptoms: convert to multi-hot encoding
    input_features = mlb.transform([symptoms])

    # Predict the encoded disease label
    predicted_label_encoded = clf.predict(input_features)[0]

    # Decode the label to get the disease name
    predicted_disease = le.inverse_transform([predicted_label_encoded])[0]

    return predicted_disease
