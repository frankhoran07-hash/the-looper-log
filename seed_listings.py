import sys
from pathlib import Path

# Automatically add project root to import path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from db import ingest_listing

NEW_LISTINGS = [
    {
        "model_slug": "mainship-395-400-trawler",
        "data": {
            "title": "2006 Mainship 400 Trawler",
            "year": 2006,
            "current_asking_price": 195000,
            "source_site": "curtisstokes",
            "source_url": "https://www.curtisstokes.com/example-mainship-400",
            "location_city": "Fort Myers",
            "location_state": "FL",
            "currency": "USD"
        }
    },
    {
        "model_slug": "grand-banks-42-classic",
        "data": {
            "title": "1994 Grand Banks 42 Classic",
            "year": 1994,
            "current_asking_price": 179000,
            "source_site": "denison",
            "source_url": "https://www.denisonyachting.com/example-gb42",
            "location_city": "Annapolis",
            "location_state": "MD",
            "currency": "USD"
        }
    }
]

for item in NEW_LISTINGS:
    ingest_listing(item["data"], model_slug=item["model_slug"])