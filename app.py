import os
import socket
from pathlib import Path

import joblib
import pandas as pd
from flask import Flask, jsonify, render_template, request
from flask_cors import CORS

from config import HOST, PORT
from utils import get_server_ip

MODEL_PATH = Path(__file__).parent / "car_price_model.joblib"
CURRENT_YEAR = 2025

app = Flask(__name__)
CORS(app)
pipeline = None


def load_model():
    global pipeline
    if pipeline is None:
        if not MODEL_PATH.exists():
            raise FileNotFoundError(
                f"Model not found at {MODEL_PATH}. Run: python3 train_model.py"
            )
        pipeline = joblib.load(MODEL_PATH)
    return pipeline


def predict_price(brand, year, kms_driven, fuel, transmission, owner):
    model = load_model()
    age = CURRENT_YEAR - int(year)
    sample = pd.DataFrame([{
        "brand": brand.lower(),
        "kms_driven": int(kms_driven),
        "fuel": fuel.lower(),
        "transmission": transmission.lower(),
        "owner": owner.lower(),
        "age": age,
    }])
    return float(model.predict(sample)[0])


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    required = ["brand", "year", "kms", "fuel", "transmission", "owner"]
    missing = [field for field in required if not data.get(field)]
    if missing:
        return jsonify({"error": f"Missing fields: {', '.join(missing)}"}), 400

    try:
        price = predict_price(
            brand=data["brand"],
            year=data["year"],
            kms_driven=data["kms"],
            fuel=data["fuel"],
            transmission=data["transmission"],
            owner=data["owner"],
        )
        return jsonify({"price": price})
    except FileNotFoundError as exc:
        return jsonify({"error": str(exc)}), 500
    except Exception as exc:
        return jsonify({"error": f"Prediction failed: {exc}"}), 500


if __name__ == "__main__":
    load_model()
    port = int(os.environ.get("PORT", PORT))
    server_ip = get_server_ip()
    url = f"http://{server_ip}:{port}"
    print(f"Open in browser: {url}")
    app.run(debug=True, host=HOST, port=port, use_reloader=False)
