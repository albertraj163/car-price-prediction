# Car Price Predictor

Predict used car prices using a Random Forest machine learning model with a clean web UI.

## Features

- Train ML model from car dataset
- Predict price via CLI or web interface
- HTML/CSS UI with brand, year, kms, fuel, transmission, and owner inputs
- **100% free** — run on your own computer or PythonAnywhere (no Render)

## Quick Start — Own Server (Free)

```bash
pip install -r requirements.txt
./run_server.sh
```

Open: **http://127.0.0.1:5050**

```bash
./stop_server.sh      # stop server
./status_server.sh    # check if running
```

## Live Website — PythonAnywhere (Free, Always Online)

No Render. Full free cloud hosting: [DEPLOY.md](DEPLOY.md)

## Local Development

```bash
./start.sh
```

## CLI Prediction

```bash
python3 predict.py --brand maruti --year 2014 --kms 50000 --fuel petrol --transmission manual --owner first
```

## Project Structure

| File | Description |
|------|-------------|
| `run_server.sh` | Start app in background (free, own server) |
| `stop_server.sh` | Stop background server |
| `wsgi.py` | PythonAnywhere config |
| `train_model.py` | Train and save the model |
| `predict.py` | Command-line prediction |
| `app.py` | Flask web server |
| `templates/index.html` | Web UI |
| `static/style.css` | UI styling |

## Tech Stack

- Python, scikit-learn, pandas, Flask, gunicorn
