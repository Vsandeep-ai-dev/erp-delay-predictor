import os
from flask import Flask, render_template, request, send_file
import pandas as pd
import joblib
from datetime import datetime

app = Flask(__name__)

# Load the trained model
model_path = 'model/your_model.pkl'
if not os.path.exists(model_path):
    raise FileNotFoundError("🚫 Model file not found! Please train it first.")

model = joblib.load(model_path)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return "No file part in the request"
    
    file = request.files['file']
    if file.filename == '':
        return "No selected file"

    try:
        df = pd.read_csv(file)

        # Predict
        predictions = model.predict(df)
        df['Predicted Delay'] = predictions

        # Save result to CSV
        output_path = f'output/predicted_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'
        os.makedirs('output', exist_ok=True)
        df.to_csv(output_path, index=False)

        table_html = df.to_html(classes='table table-bordered table-striped', index=False)

        return render_template('results.html', table=table_html, download_link=output_path)
    except Exception as e:
        return f"Error processing file: {str(e)}"

@app.route('/download/<path:filename>')
def download_file(filename):
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
