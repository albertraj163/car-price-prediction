# Car Price Predictor

Predict used car prices using a Random Forest machine learning model with a clean web UI.

## Features

- Train ML model from car dataset
- Predict price via CLI or web interface
- HTML/CSS UI with brand, year, kms, fuel, transmission, and owner inputs

## Setup

```bash
pip install -r requirements.txt
python3 train_model.py
python3 app.py
```

Open in browser: **http://127.0.0.1:5050**

## CLI Prediction

```bash
python3 predict.py --brand maruti --year 2014 --kms 50000 --fuel petrol --transmission manual --owner first
```

## Project Structure

| File | Description |
|------|-------------|
| `train_model.py` | Train and save the model |
| `predict.py` | Command-line prediction |
| `app.py` | Flask web server |
| `utils.py` | Data loading and preprocessing |
| `templates/index.html` | Web UI |
| `static/style.css` | UI styling |
| `car_data_sample.csv` | Sample training data |

## Tech Stack

- Python, scikit-learn, pandas
- Flask
- HTML, CSS
