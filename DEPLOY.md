# Free Hosting Guide (No Render) — Tamil + English

Render **theva illa**. Intha 2 free methods use pannunga.

---

## Method 1 — Own computer la run (100% free, full control)

Unga computer/server (`golden-base`) la background la run pannalam.

### Start
```bash
cd ~/Documents/car-price-prediction-main
pip install -r requirements.txt
./run_server.sh
```

### Open pannunga
- Same computer: **http://127.0.0.1:5050**
- Same WiFi phone/laptop: **http://YOUR_IP:5050** (terminal la IP show aagum)

### Stop / Check
```bash
./stop_server.sh      # stop
./status_server.sh    # running-a check
```

Computer on irundha mattum work aagum. Background la run aagudhu — terminal close pannalum ok.

---

## Method 2 — PythonAnywhere (100% free cloud, always online)

Local computer off irundhalum work aagum. Render maari third-party paid service **illa**.

### Step 1 — Account
1. Open: **https://www.pythonanywhere.com/registration/register/beginner/**
2. Free account create pannunga

### Step 2 — Code upload
1. **Consoles** → **Bash** open pannunga
2. Run:
```bash
git clone https://github.com/albertraj163/car-price-prediction.git
cd car-price-prediction
pip install --user -r requirements.txt
```

### Step 3 — Web app setup
1. **Web** tab → **Add a new web app**
2. **Manual configuration** → **Python 3.10** → Next
3. **Virtualenv**: optional skip
4. **Source code**: `/home/YOUR_USERNAME/car-price-prediction`
5. **WSGI configuration file** click → edit pannunga:

```python
import sys
path = '/home/YOUR_USERNAME/car-price-prediction'
if path not in sys.path:
    sys.path.insert(0, path)

from app import app as application
```

(`YOUR_USERNAME` replace pannunga — PythonAnywhere username)

6. **Save** → **Reload** click pannunga

### Step 4 — Live URL
```
https://YOUR_USERNAME.pythonanywhere.com
```

Phone, office, enga irunthalum open pannalam. **Fully free.**

---

## Render delete panna

Render la deploy pannirundha:
1. **https://dashboard.render.com** open pannunga
2. Service select → **Settings** → **Delete Web Service**

---

## Quick compare

| Method | Cost | Computer on venuma? | Enga irundhum open? |
|--------|------|---------------------|---------------------|
| `run_server.sh` | Free | Yes | Same network |
| PythonAnywhere | Free | No | Yes, anywhere |
