# Car Price Predictor

Predict used car prices using Machine Learning — localhost maari full-a work aagum.

## Open App

### http://192.168.1.20:5554

Form fill panni **Get Price Estimate** click pannunga — price varum.

## Start Server

```bash
cd ~/Documents/car-price-prediction-main
pip install -r requirements.txt
./run_server.sh
```

Terminal la link show aagum. Browser la open pannunga.

```bash
./status_server.sh    # running check
./stop_server.sh      # stop
./start.sh            # foreground (development)
```

## Settings

| Setting | Value |
|---------|-------|
| Port | `5554` → change in `config.py` |
| IP | `192.168.1.20` (server network IP) |
| Link | `http://192.168.1.20:5554` |

## GitHub

https://github.com/albertraj163/car-price-prediction
