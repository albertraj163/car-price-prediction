# Car Price Predictor

Predict used car prices using Machine Learning.

## Links

| | URL |
|---|---|
| **Open App** | **https://albertraj163.github.io/car-price-prediction/** |
| GitHub Repo | https://github.com/albertraj163/car-price-prediction |
| Live API | https://albertraj163-car-price-prediction.hf.space |

## Features

- Web UI — brand, year, kms, fuel, transmission, owner
- Random Forest ML model
- Free hosting via GitHub Pages + Hugging Face

## Run Locally

```bash
pip install -r requirements.txt
./run_public.sh    # public internet link
./run_server.sh    # LAN only (192.168.x:5554)
```

## Deploy Live Link (one time)

```bash
./deploy_hf.sh
```

GitHub Pages auto-deploys on every push to `main`.

## CLI

```bash
python3 predict.py --brand maruti --year 2014 --kms 50000 --fuel petrol --transmission manual --owner first
```

## Tech Stack

Python · Flask · scikit-learn · GitHub Pages · Hugging Face Spaces
