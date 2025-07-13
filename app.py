from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)
model = joblib.load("model.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        try:
            inputs = [
                float(request.form['age']),
                float(request.form['studytime']),
                float(request.form['failures']),
                float(request.form['absences']),
                float(request.form['G1']),
                float(request.form['G2']),
            ]
            prediction = model.predict([inputs])[0]
            prediction = round(prediction, 2)
        except:
            prediction = "Invalid input"
    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
