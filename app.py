import os
if not os.path.exists('model/your_model.pkl'):
    raise FileNotFoundError("🚫 Model file not found! Please train it first using the training script.")
from flask import Flask, render_template, request, send_file
import pandas as pd
import joblib
import os
from datetime import datetime

app = Flask(__name__)
model = joblib.load('model/your_model.pkl')  # adjust model path

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['file']
    if not file:
        return "Please upload a file!"

    df = pd.read_csv(file)

    # 🧠 Run ML model prediction
    predictions = model.predict(df)
    df['Predicted Delay'] = predictions

    # Save output
    output_path = f'output/predicted_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'
    df.to_csv(output_path, index=False)

    # Show table on webpage
    table_html = df.to_html(classes='table table-bordered table-striped', index=False)

    return render_template('results.html', table=table_html, download_link=output_path)

@app.route('/download/<path:filename>')
def download_file(filename):
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
    print("Registered Routes:")
    print(app.url_map)
