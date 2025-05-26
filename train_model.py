import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer, LabelEncoder

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