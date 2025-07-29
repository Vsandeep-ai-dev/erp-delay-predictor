from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load("model/model.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        values = [float(x) for x in request.form.values()]
        arr = np.array([values])
        pred = model.predict(arr)[0]
        msg = "🚨 Delayed" if pred == 1 else "✅ On Time"
    except Exception:
        msg = "⚠️ Invalid input. Please enter numeric values."
    return render_template('index.html', prediction_text=msg)

if __name__ == "__main__":
    app.run(debug=True)

