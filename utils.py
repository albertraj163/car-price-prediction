import socket

import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer


def get_server_ip():
    try:
        for info in socket.getaddrinfo(socket.gethostname(), None, socket.AF_INET):
            ip = info[4][0]
            if ip.startswith("192."):
                return ip
    except OSError:
        pass

    probe = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        probe.connect(("192.168.1.1", 1))
        ip = probe.getsockname()[0]
        if ip.startswith("192."):
            return ip
    except OSError:
        pass
    finally:
        probe.close()

    return socket.gethostbyname(socket.gethostname())


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
