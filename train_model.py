import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
import os

# Ensure the 'model' directory exists
os.makedirs("model", exist_ok=True)

# Dummy ERP-like data (replace with real ERP data if available)
data = pd.DataFrame({
    'Material_Code': [1001, 1002, 1003, 1004],
    'Base_Unit_of_Measure': [1, 2, 1, 2],
    'Material_Group': [5, 6, 7, 5],
    'Production_Plant': [101, 102, 103, 101],
    'Storage_Location': [301, 302, 303, 301],
    'Supplier': [201, 202, 203, 201],
    'Purchasing_Organization': [401, 402, 403, 401],
    'Purchasing_Group': [501, 502, 503, 501],
    'Company_Code': [601, 602, 603, 601],
    'Document_Type': [701, 702, 703, 701],
    'Document_Date': [20200101, 20200102, 20200103, 20200101],
    'Release_Date': [20200103, 20200104, 20200105, 20200103],
    'Net_Price': [1000, 2000, 1500, 1700],
    'Currency': [1, 2, 1, 2],
    'Quantity': [10, 20, 15, 25],
    'Planned_Delivery_Time': [5, 10, 7, 6],
    'GR_Processing_Time': [2, 3, 1, 2],
    'Standard_Price': [950, 1900, 1400, 1600],
    'Delay': [0, 1, 0, 1]  # Target variable
})

# Split features and target
X = data.drop('Delay', axis=1)
y = data['Delay']

# Split data into train and test sets (optional, for future improvements)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Save the model to the model folder
joblib.dump(model, "model/delay_predictor.pkl")
print("✅ Model trained and saved successfully as 'model/delay_predictor.pkl'")
