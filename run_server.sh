#!/usr/bin/env bash
# Run app in background — free, no Render needed

cd "$(dirname "$0")"
PORT="${PORT:-5554}"
SERVER_IP=$(hostname -I | tr ' ' '\n' | grep '^192\.' | head -1)
if [ -z "$SERVER_IP" ]; then
  SERVER_IP=$(hostname -I | awk '{print $1}')
fi

if [ ! -f "car_price_model.joblib" ]; then
  echo "Training model (first time only)..."
  python3 train_model.py
fi

pkill -f "gunicorn app:app" 2>/dev/null || true
sleep 1

echo "Starting server on http://$SERVER_IP:$PORT"
nohup gunicorn app:app \
  --bind "0.0.0.0:$PORT" \
  --workers 1 \
  --timeout 120 \
  --daemon \
  --access-logfile access.log \
  --error-logfile error.log

echo ""
echo "  Server running!"
echo "  Open: http://$SERVER_IP:$PORT"
echo ""
echo "  Stop:    ./stop_server.sh"
echo "  Status:  ./status_server.sh"
echo ""
