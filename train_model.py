import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.metrics import r2_score, root_mean_squared_error
import joblib
from utils import load_data, build_pipeline

DATA_PATH = "car_data_sample.csv"
MODEL_PATH = "car_price_model.joblib"

def prepare_data(df):
    df = df.copy()
    df['age'] = 2025 - df['year']
    X = df[['brand', 'kms_driven', 'fuel', 'transmission', 'owner', 'age']]
    y = df['price']
    return X, y

def main():
    df = load_data(DATA_PATH)
    X, y = prepare_data(df)

    categorical_cols = ['brand', 'fuel', 'transmission', 'owner']

    preprocessor = build_pipeline(categorical_cols)

    model = RandomForestRegressor(n_estimators=100, random_state=42)

    pipeline = Pipeline(steps=[('preprocess', preprocessor),
                               ('model', model)])

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    pipeline.fit(X_train, y_train)

    preds = pipeline.predict(X_test)
    r2 = r2_score(y_test, preds)
    rmse = root_mean_squared_error(y_test, preds)

    print(f"R2: {r2:.3f}, RMSE: {rmse:.2f}")

    joblib.dump(pipeline, MODEL_PATH)
    print(f"Saved trained model to {MODEL_PATH}")

if __name__ == "__main__":
    main()
