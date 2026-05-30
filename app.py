import os
import socket
from pathlib import Path

import joblib
import pandas as pd
from flask import Flask, jsonify, render_template, request

MODEL_PATH = Path(__file__).parent / "car_price_model.joblib"
CURRENT_YEAR = 2025

app = Flask(__name__)
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


def find_free_port(start=5050, attempts=20):
    for port in range(start, start + attempts):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            try:
                sock.bind(("0.0.0.0", port))
                return port
            except OSError:
                continue
    raise RuntimeError(f"No free port found between {start} and {start + attempts - 1}")


if __name__ == "__main__":
    load_model()
    preferred = int(os.environ.get("PORT", 5050))
    port = find_free_port(preferred)
    if port != preferred:
        print(f"Port {preferred} is busy, using port {port} instead.")
    print(f"Open in browser: http://127.0.0.1:{port}")
    app.run(debug=True, host="0.0.0.0", port=port, use_reloader=False)
