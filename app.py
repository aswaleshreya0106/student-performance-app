from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

with open("model.pkl", "rb") as file:
    model = pickle.load(file)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        try:
            age = float(request.form['age'])
            studytime = float(request.form['studytime'])
            failures = float(request.form['failures'])
            absences = float(request.form['absences'])
            g1 = float(request.form['G1'])
            g2 = float(request.form['G2'])

            features = [[age, studytime, failures, absences, g1, g2]]
            prediction = round(model.predict(features)[0], 2)
        except:
            prediction = "Invalid input."
    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
