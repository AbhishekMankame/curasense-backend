import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

# Load dataset
df = pd.read_csv("data/symptom_disease_data.csv")

# Split symptoms string into list
df['symptoms'] = df['symptoms'].apply(lambda x: x.split(';'))

# Create MultLabelBinarizer for symptoms (multi-hot encoding)
mlb = MultiLabelBinarizer()
X = mlb.fit_transform(df['symptoms'])

# Encode disease labels
le = LabelEncoder()
y = le.fit_transform(df['disease'])

print("Feature names (symptoms):", mlb.classes_)
print("Encoded features shape:", X.shape)
print("Encoded labels:", y)

# Train Random Forest classifier
clf = RandomForestClassifier(n_estimators=100, random_state = 42)
clf.fit(X,y)

# Create 'model' folder if it doesn't exist
if not os.path.exists("model"):
    os.makedirs("model")

# Save the trained model and encoders for later use
joblib.dump(clf, "model/disease_predictor.pkl")
joblib.dump(mlb, "model/symptom_encoder.pkl")
joblib.dump(le, "model/disease_label_encoder.pkl")

print("Model and encoders saved successfully!- ")