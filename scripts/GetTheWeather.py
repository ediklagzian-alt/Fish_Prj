import os
import json
import time
from pathlib import Path
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

URL = "https://api.openweathermap.org/data/2.5/weather"
OUT_DIR = Path("data/raw/weather")
OUT_DIR.mkdir(parents=True, exist_ok=True)

CITIES = [
    {"name": "moscow",    "lat": 55.7558, "lon": 37.6173},
    {"name": "spb",       "lat": 59.9343, "lon": 30.3351},
    {"name": "krasnodar", "lat": 45.0355, "lon": 38.9753},
]

for city in CITIES:
    params = {
        "lat": city["lat"],
        "lon": city["lon"],
        "appid": API_KEY,
        "units": "metric",
        "lang": "ru",
    }
    r = requests.get(URL, params=params, timeout=10)
    r.raise_for_status()
    data = r.json()

    out_file = OUT_DIR / f"{city['name']}.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"{city['name']}: {data['main']['temp']}°C, "
          f"{data['main']['pressure']} hPa, "
          f"ветер {data['wind']['speed']} м/с → {out_file}")

    time.sleep(1.2)