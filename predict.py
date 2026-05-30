import argparse
import joblib
import pandas as pd

MODEL_PATH = "car_price_model.joblib"
CURRENT_YEAR = 2025


def predict_price(brand, year, kms_driven, fuel, transmission, owner, model_path=MODEL_PATH):
    pipeline = joblib.load(model_path)
    age = CURRENT_YEAR - year
    sample = pd.DataFrame([{
        "brand": brand.lower(),
        "kms_driven": kms_driven,
        "fuel": fuel.lower(),
        "transmission": transmission.lower(),
        "owner": owner.lower(),
        "age": age,
    }])
    return pipeline.predict(sample)[0]


def main():
    parser = argparse.ArgumentParser(description="Predict car price")
    parser.add_argument("--brand", required=True, help="e.g. maruti, honda, hyundai")
    parser.add_argument("--year", type=int, required=True, help="e.g. 2018")
    parser.add_argument("--kms", type=int, required=True, help="kilometers driven, e.g. 50000")
    parser.add_argument("--fuel", required=True, choices=["petrol", "diesel"], help="fuel type")
    parser.add_argument("--transmission", required=True, choices=["manual", "automatic"])
    parser.add_argument("--owner", required=True, choices=["first", "second", "third"])
    args = parser.parse_args()

    price = predict_price(
        brand=args.brand,
        year=args.year,
        kms_driven=args.kms,
        fuel=args.fuel,
        transmission=args.transmission,
        owner=args.owner,
    )
    print(f"Predicted price: ₹{price:,.0f}")


if __name__ == "__main__":
    main()
