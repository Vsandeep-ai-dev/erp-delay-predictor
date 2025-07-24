from flask import Flask, request, render_template
import numpy as np
import pickle

app = Flask(__name__)

# Load your model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Read inputs from the form
        features = [float(x) for x in request.form.values()]
        final = [np.array(features)]
        prediction = model.predict(final)
        output = round(prediction[0], 2)

        return render_template('result.html', prediction_text=f'Estimated ERP Delay: {output} days')
    except:
        return render_template('result.html', prediction_text="⚠️ Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    app.run(debug=True)
