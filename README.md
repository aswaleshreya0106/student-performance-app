# 🎓 Student Performance Predictor (Flask Web App)

This project predicts a student's final exam grade (G3) using inputs like age, study time, past grades, and absences. It's built with **Flask** and deployable via **Render**.

## 🚀 Features
- Simple web form UI
- Predicts G3 using a trained regression model
- Built with Flask, scikit-learn, HTML, CSS

## 🛠 How to Use Locally
1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Make sure `model.pkl` is present (trained using `train_model.py`)
4. Run app: `python app.py`
5. Visit: `http://127.0.0.1:5000`

## 🌐 Live Deployment (Render)
- Push all files to GitHub
- Go to [render.com](https://render.com)
- Create new Web Service
- Use:
  - **Build Command**: `pip install -r requirements.txt`
  - **Start Command**: `python app.py`

## 📂 Files
- `app.py` – Main Flask app
- `model.pkl` – Trained ML model
- `templates/index.html` – Web form UI
- `static/style.css` – Page styling
- `requirements.txt` – Dependencies
