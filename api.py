from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)
 HEAD
model = joblib.load("model/delay_predictor.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        features = [
            "Material_Code", "Base_Unit_of_Measure", "Material_Group", "Production_Plant", "Storage_Location",
            "Supplier", "Purchasing_Organization", "Purchasing_Group", "Company_Code", "Document_Type",
            "Document_Date", "Release_Date", "Net_Price", "Currency", "Quantity",
            "Planned_Delivery_Time", "GR_Processing_Time", "Standard_Price"
        ]
        input_data = np.array([[data[feature] for feature in features]])
        prediction = model.predict(input_data)
        return jsonify({"prediction": int(prediction[0])})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Load trained model
model = joblib.load("model/delay_predictor.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    try:
        features = [
            data['quantity'],
            data['price'],
            data['rating'],
            data['vendor_score'],
            data['ship_speed'],
            data['demand']
        ]
        input_data = np.array([features])
        prediction = model.predict(input_data)[0]
        return jsonify({'prediction': int(prediction)})
    except KeyError as e:
        return jsonify({'error': f'Missing key: {e}'}), 400
 a3764319c2e129180a4a7e5a678214f58cf83244

if __name__ == "__main__":
    app.run(debug=True)
