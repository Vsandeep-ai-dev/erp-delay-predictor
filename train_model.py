
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
<<<<<<< HEAD
import pickle
import os

# Ensure the 'model' directory exists
os.makedirs("model", exist_ok=True)

# Dummy Data (replace with real ERP data in the future)
data = pd.DataFrame({
    'Material_Code': [1001, 1002],
    'Base_Unit_of_Measure': [1, 2],
    'Material_Group': [5, 6],
    'Production_Plant': [101, 102],
    'Storage_Location': [301, 302],
    'Supplier': [201, 202],
    'Purchasing_Organization': [401, 402],
    'Purchasing_Group': [501, 502],
    'Company_Code': [601, 602],
    'Document_Type': [701, 702],
    'Document_Date': [20200101, 20200102],
    'Release_Date': [20200103, 20200104],
    'Net_Price': [1000, 2000],
    'Currency': [1, 2],
    'Quantity': [10, 20],
    'Planned_Delivery_Time': [5, 10],
    'GR_Processing_Time': [2, 3],
    'Standard_Price': [950, 1900],
    'Delay': [0, 1]  # Target variable
})

# Split features and target
X = data.drop('Delay', axis=1)
y = data['Delay']

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
 a3764319c2e129180a4a7e5a678214f58cf83244

# Train the model
model = RandomForestClassifier()
model.fit(X, y)

<<<<<<< HEAD
# Save model inside "model" folder with the correct name
with open('model/delay_predictor.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as model/delay_predictor.pkl")


# Save model
os.makedirs("model", exist_ok=True)
joblib.dump(model, "model/delay_predictor.pkl")
print("✅ Model trained and saved as model/delay_predictor.pkl")
 a3764319c2e129180a4a7e5a678214f58cf83244
