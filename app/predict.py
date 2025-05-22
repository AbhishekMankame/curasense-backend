from typing import List

# Simple dummy mapping of symptoms to disease
SYMPTOM_DISEASE_MAP = {
    "fever": ["Flu", "Common Cold", "COVID-19"],
    "cough": ["Common Cold", "Flu", "Bronchitis"],
    "headache": ["Migraine", "Flu", "Tension Headache"],
    "fatigue": ["Anemia", "Flu", "COVID-19"],
    "rash": ["Allergy", "Chickenpox"],
    # Add more mappings as needed
}

def run_prediction(symptoms: List[str]) -> str:
    disease_scores = {}

    for symptom in symptoms:
        possible_diseases = SYMPTOM_DISEASE_MAP.get(symptom.lower(), [])
        for disease in possible_diseases:
            disease_scores[disease] = disease_scores.get(disease, 0) + 1

    if not disease_scores:
        return "No matching disease found"
    
    # Pick disease with highest score
    predicted_disease = max(disease_scores, key=disease_scores.get)
    return predicted_disease