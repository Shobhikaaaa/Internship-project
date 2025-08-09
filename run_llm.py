from typing import Any
import httpx # Kept as per your provided imports, though not directly used in this snippet
from mcp.server.fastmcp import FastMCP

# Assuming get_hotel_metrics is defined in fetch_data.py
# If you want to use the hardcoded data directly in this file,
# you can remove the import of get_hotel_metrics and define the data inline.
from fetch_data import get_hotel_metrics

# Initialize FastMCP server with app id "llm_app"
app = FastMCP("llm_app")

# Define the resource directly as an asynchronous function.
# FastMCP automatically handles JSON serialization for dictionaries returned by resources.
@mcp.tool()
async def get_hotel_metrics_resource() -> dict[str, Any]:
    """
    Retrieves hotel metrics data.
    This function serves as the resource handler for the specified URI.
    It returns a dictionary, which FastMCP will automatically serialize to JSON.
    """
    try:
        # If you want to use the hardcoded data from your example, uncomment and use this:
        # metrics = {
        #     "occupancy": 89.7,
        #     "revenue": 120000,
        #     "date": "2025-07-07"
        # }
        # Otherwise, continue to use your get_hotel_metrics() function:
        metrics = get_hotel_metrics()
        return metrics
    except Exception as e:
        print(f"Error fetching hotel metrics: {e}")
        return {
            "error": str(e),
            "message": "Failed to retrieve hotel metrics."
        }

# IMPORTANT: To run this application with Uvicorn, you must specify
# the 'asgi_app' attribute of the FastMCP instance.
# Use the command: uvicorn run_llm:app.asgi_app --port 3333 --reload
