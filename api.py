from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True)
