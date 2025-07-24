import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import pickle

# Dummy Data (you can replace with real ERP dataset)
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
    'Delay': [0, 1]  # Target
})

X = data.drop('Delay', axis=1)
y = data['Delay']

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Save the model to disk
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as model.pkl")
