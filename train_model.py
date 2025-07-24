import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
import os

# Load your data
df = pd.read_csv("data/erp_data.csv")

# Example: using Quantity, UnitPrice, WarehouseRating, VendorScore, ShippingSpeed, ItemDemand
X = df[["Quantity", "UnitPrice", "WarehouseRating", "VendorScore", "ShippingSpeed", "ItemDemand"]]
y = df["Delayed"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = RandomForestClassifier()
clf.fit(X_train, y_train)

os.makedirs("model", exist_ok=True)
joblib.dump(clf, "model/model.pkl")

print("✅ Model trained and saved.")
