#!/usr/bin/env bash
cd "$(dirname "$0")"

source "$(dirname "$0")/server_env.sh"

if [ ! -f "car_price_model.joblib" ]; then
  echo "Training model (first time only)..."
  python3 train_model.py
fi

pkill -f "gunicorn app:app" 2>/dev/null || true
sleep 1

echo "Starting server..."
nohup gunicorn app:app \
  --bind "${HOST}:${PORT}" \
  --workers 1 \
  --timeout 120 \
  --daemon \
  --access-logfile access.log \
  --error-logfile error.log

echo ""
echo "  Server running!"
echo "  Open: http://${SERVER_IP}:${PORT}"
echo ""
echo "  Stop:   ./stop_server.sh"
echo "  Status: ./status_server.sh"
echo ""
