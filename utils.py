import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

def load_data(path="car_data_sample.csv"):
    df = pd.read_csv(path)
    return df

def build_pipeline(categorical_cols):
    cat_transformer = OneHotEncoder(handle_unknown="ignore", sparse_output=False)
    preprocessor = ColumnTransformer(
        transformers=[("cat", cat_transformer, categorical_cols)],
        remainder='passthrough'
    )
    return preprocessor
