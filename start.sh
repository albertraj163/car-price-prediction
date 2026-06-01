#!/usr/bin/env bash
cd "$(dirname "$0")"
source "$(dirname "$0")/server_env.sh"

if [ ! -f "car_price_model.joblib" ]; then
  echo "Training model (first time only)..."
  python3 train_model.py
fi

python3 app.py
