# generate_checkin_data.py

import json
from datetime import datetime, timedelta
import random

SCHEMAS = ["CHECKIN", "PRECHECKIN", "EREGISTRATION"]

def generate_counts():
    def r(): return random.randint(0, 10)
    return {
        "pwaFailureCount": r(),
        "pwaSuccessCount": r(),
        "iptvFailureCount": r(),
        "iptvSuccessCount": r(),
        "kioskFailureCount": r(),
        "kioskSuccessCount": r(),
        "tabletFailureCount": r(),
        "tabletSuccessCount": r(),
        "mobileAppFailureCount": r(),
        "mobileAppSuccessCount": r(),
        "staffConnectFailureCount": r(),
        "staffConnectSuccessCount": r(),
    }

def compute_totals(entry):
    entry["totalFailureCount"] = (
        entry["pwaFailureCount"] +
        entry["iptvFailureCount"] +
        entry["kioskFailureCount"] +
        entry["tabletFailureCount"] +
        entry["mobileAppFailureCount"] +
        entry["staffConnectFailureCount"]
    )
    entry["totalSuccessCount"] = (
        entry["pwaSuccessCount"] +
        entry["iptvSuccessCount"] +
        entry["kioskSuccessCount"] +
        entry["tabletSuccessCount"] +
        entry["mobileAppSuccessCount"] +
        entry["staffConnectSuccessCount"]
    )
    return entry

def generate_data(schema):
    data = []
    for i in range(20):
        day = datetime.today() - timedelta(days=i)
        base = generate_counts()
        complete = compute_totals(base)
        complete["date"] = day.strftime("%Y-%m-%d")
        complete["taj"] = f"taj-{schema.lower()}-{i+1}"
        data.append(complete)
    return data

for schema in SCHEMAS:
    records = generate_data(schema)
    with open(f"{schema.lower()}_data.json", "w") as f:
        json.dump(records, f, indent=2)
