# ERP Delay Predictor

A web-based Machine Learning application designed to predict delays in ERP processes using logistic regression. Built with Flask, Bootstrap, and a clean modular architecture for scalability.

---

## 🚀 Features

- Predict ERP delays using trained ML model
- Intuitive Bootstrap UI
- Modular structure for maintainability
- REST API for prediction
- Cleaned and preprocessed ERP dataset

---

## 🛠️ Tech Stack

- Python (Flask)
- Scikit-learn
- Pandas, NumPy
- HTML/CSS (Bootstrap)
- GitHub + Git

---

## 📁 Project Structure

```
erp-delay-predictor/
│
├── app.py               # Main Flask app
├── cleaner.py           # Data cleaning logic
├── predict_api.py       # Prediction endpoint
├── train_model.py       # Model training script
├── erp_data.csv         # Dataset
├── requirements.txt     # Dependencies
│
├── data/                # (If additional data files)
├── model/               # Trained ML model (pickle)
├── static/              # CSS, JS, Bootstrap assets
└── templates/           # HTML templates
```

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/Vsandeep-ai-dev/erp-delay-predictor.git
cd erp-delay-predictor

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt
```

---

## 🧠 How It Works

1. Upload or input data via UI or API.
2. Data is cleaned using `cleaner.py`.
3. Prediction is made using the trained model.
4. Output is shown in browser.

---

## ▶️ Run the App

```bash
python app.py
```

Visit [http://localhost:5000](http://localhost:5000) in your browser.

---

## 📽️ Demo Video

▶️ [Add your YouTube or Loom demo link here]

---

## 🧪 Sample Prediction API (Postman)

- **Endpoint:** `/predict_api`
- **Method:** POST
- **Payload Example:**
```json
{
  "Column1": value1,
  "Column2": value2,
  ...
}
```

---

## 📌 Topics

- Machine Learning
- Flask Web App
- ERP Systems
- Logistic Regression
- API Deployment
- UI with Bootstrap

---

## 🔒 Repository Status

> ✅ Public and ready to showcase.

---

## 📧 Contact

- Developer: [Sandeep Reddy](mailto:your-email@example.com)
- GitHub: [@Vsandeep-ai-dev](https://github.com/Vsandeep-ai-dev)

---


