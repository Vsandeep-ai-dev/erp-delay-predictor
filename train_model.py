import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

# Sample dummy data
data = pd.DataFrame({
    'quantity': [10, 20, 30, 40, 50],
    'price': [5.0, 10.0, 15.0, 20.0, 25.0],
    'rating': [1, 2, 3, 4, 5],
    'vendor_score': [3, 6, 7, 8, 9],
    'ship_speed': [1, 2, 3, 2, 1],
    'demand': [20, 40, 60, 80, 100],
    'delay': [0, 1, 0, 1, 0]
})

X = data.drop("delay", axis=1)
y = data["delay"]

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Save model
os.makedirs("model", exist_ok=True)
joblib.dump(model, "model/delay_predictor.pkl")
print("✅ Model trained and saved as model/delay_predictor.pkl")
