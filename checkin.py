# mcp_tools.py

import json
from datetime import datetime
from typing import Optional
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("checkin")

def load_json(filename):
    with open(filename) as f:
        return json.load(f)

CHECKIN_DATA = load_json("./checkin_data.json")
PRECHECKIN_DATA = load_json("./precheckin_data.json")
EREGISTRATION_DATA = load_json("./eregistration_data.json")

def get_today_entry(data) -> Optional[dict]:
    today = datetime.today().strftime("%Y-%m-%d")
    for entry in data:
        if entry["date"] == today:
            return entry
    return None

def format_output(entry: dict) -> str:
    return f"TAJ: {entry['taj']}\nDate: {entry['date']}\n" + json.dumps(entry, indent=2)

@mcp.tool()
async def get_checkin_data() -> str:
    """Get today's CHECKIN data from local JSON."""
    entry = get_today_entry(CHECKIN_DATA)
    return format_output(entry) if entry else "No CHECKIN data for today."

@mcp.tool()
async def get_precheckin_data() -> str:
    """Get today's PRECHECKIN data from local JSON."""
    entry = get_today_entry(PRECHECKIN_DATA)
    return format_output(entry) if entry else "No PRECHECKIN data for today."

@mcp.tool()
async def get_eregistration_data() -> str:
    """Get today's EREGISTRATION data from local JSON."""
    entry = get_today_entry(EREGISTRATION_DATA)
    return format_output(entry) if entry else "No EREGISTRATION data for today."

if __name__ == "__main__":
    # Initialize and run the server
    print("running the server")
    mcp.run(transport='stdio')