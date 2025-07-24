import streamlit as st
import joblib
import numpy as np

st.title("🚚 ERP Delay Predictor")
st.write("Enter order details to predict delivery delay.")

# Load model
model = joblib.load("model/delay_predictor.pkl")

# Input form
quantity = st.slider("Order Quantity", 1, 500, 100)
price = st.slider("Unit Price", 1.0, 100.0, 10.0)
rating = st.slider("Warehouse Rating", 1, 5, 3)
vendor_score = st.slider("Vendor Score", 1, 10, 5)
ship_speed = st.selectbox("Shipping Speed", [1, 2, 3])
demand = st.slider("Item Demand", 1, 100, 50)

if st.button("Predict Delay"):
    input_data = np.array([[quantity, price, rating, vendor_score, ship_speed, demand]])
    result = model.predict(input_data)[0]
    st.success("🔴 Delayed" if result == 1 else "🟢 On Time")