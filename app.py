from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
import os

app = Flask(__name__)

MODEL_PATH = os.path.join(os.path.dirname(__file__), "model", "fraud_model.pkl")
model = None

def load_model():
    global model
    if os.path.exists(MODEL_PATH):
        with open(MODEL_PATH, "rb") as f:
            model = pickle.load(f)
        print("Model loaded.")
    else:
        print("Warning: model not found. Run model/train.py first.")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if model is None:
        return jsonify({"error": "Model not loaded. Run model/train.py first."}), 503

    data = request.get_json()

    merchant_risk = {
        "grocery": 0.1, "gas": 0.3, "online": 0.6,
        "travel": 0.5, "electronics": 0.7, "atm": 0.9
    }

    features = np.array([[
        float(data.get("amount", 0)),
        float(data.get("hour", 12)),
        float(data.get("distance", 0)),
        float(data.get("velocity", 1)),
        1.0 if data.get("card_present") == "no" else 0.0,
        1.0 if data.get("foreign") == "yes" else 0.0,
        1.0 if data.get("new_merchant") == "yes" else 0.0,
        merchant_risk.get(data.get("merchant", "grocery"), 0.3),
    ]])

    prob = model.predict_proba(features)[0][1]
    score = round(float(prob) * 100, 1)

    if score < 30:
        verdict = "safe"
        message = "Transaction looks normal. Safe to approve."
    elif score < 65:
        verdict = "review"
        message = "Elevated risk — flag for secondary review."
    else:
        verdict = "fraud"
        message = "High fraud probability — decline and alert cardholder."

    return jsonify({"score": score, "verdict": verdict, "message": message})

if __name__ == "__main__":
    load_model()
    app.run(debug=True)