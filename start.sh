#!/usr/bin/env bash
cd "$(dirname "$0")"
export PORT="${PORT:-5554}"
echo ""
echo "  Car Price Predictor starting..."
echo ""

if [ ! -f "car_price_model.joblib" ]; then
  echo "  Model not found. Training first (one time only)..."
  python3 train_model.py
  echo ""
fi

python3 app.py
