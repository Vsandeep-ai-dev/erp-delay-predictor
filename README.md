# ERP Delay Predictor 🚚

Predict whether an order will be delayed using features like quantity, price, warehouse rating, etc.

## Features
- Trained with RandomForestClassifier
- Live Streamlit web app

## Setup
```bash
pip install -r requirements.txt
python model/train_model.py
streamlit run app.py