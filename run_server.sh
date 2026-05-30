#!/usr/bin/env bash
# Run app in background — free, no Render needed

cd "$(dirname "$0")"

if [ ! -f "car_price_model.joblib" ]; then
  echo "Training model (first time only)..."
  python3 train_model.py
fi

# Stop old instance if running
pkill -f "gunicorn app:app" 2>/dev/null || true
sleep 1

echo "Starting server on http://0.0.0.0:5050"
nohup gunicorn app:app \
  --bind 0.0.0.0:5050 \
  --workers 1 \
  --timeout 120 \
  --daemon \
  --access-logfile access.log \
  --error-logfile error.log

echo ""
echo "  Server running in background!"
echo "  Local:   http://127.0.0.1:5050"
echo "  Network: http://$(hostname -I | awk '{print $1}'):5050"
echo ""
echo "  Stop:    ./stop_server.sh"
echo "  Status:  ./status_server.sh"
echo ""
