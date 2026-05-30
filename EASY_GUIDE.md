# Car Price Predictor - Easy Guide (Tamil + English)

## App use panna (NO code typing!)

### Step 1 - Start app
Terminal open panni run pannunga:

```bash
cd ~/Documents/car-price-prediction-main
./start.sh
```

### Step 2 - Browser open pannunga
Terminal la URL varum, adha copy panni browser la paste pannunga:
```
http://127.0.0.1:5050
```

### Step 3 - Form fill pannunga
- Brand select pannunga (dropdown)
- Year select pannunga
- Kms type pannunga
- Fuel, Transmission, Owner select pannunga
- **Get Price Estimate** button click pannunga

Done! Price right side la show aagum. Command line use panna theva illa!

---

## GitHub-ku upload panna (Easy)

### Method 1 - Script use pannunga (recommended)

```bash
cd ~/Documents/car-price-prediction-main
./github_upload.sh
```

Browser open aagum. Login pannitu code paste pannunga. Done!

### Method 2 - Website la manual (no terminal commands)

1. Browser la open pannunga: https://github.com/new
2. Repository name: `car-price-prediction`
3. Public select pannitu **Create repository** click
4. **uploading an existing file** link click pannunga
5. Intha folder la irukura files ellam drag & drop pannunga:
   - app.py, train_model.py, predict.py, utils.py
   - requirements.txt, README.md
   - car_data_sample.csv, car_price_model.joblib
   - templates/ folder
   - static/ folder
6. **Commit changes** click pannunga

Done! GitHub la ellam upload aagidum.

---

## Stop panna
Terminal la `Ctrl + C` press pannunga
