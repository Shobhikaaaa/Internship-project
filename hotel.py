from typing import Any
import httpx # Kept as per your provided imports
from mcp.server.fastmcp import FastMCP # FastMCP is imported

# This function is from your original code, kept as is.
# Note: It's async but currently not used by the main resource.
async def make_nws_request(url: str) -> dict[str, Any] | None:
    headers = {
        "x-api-key": "da2-hpf5f2lxyjed7gha7rrxhfkguq",
        "Content-Type": "application/json"
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except Exception:
            return None

# Initialize FastMCP server
# Using 'mcp' as the variable name as per your request.
mcp = FastMCP(name="hotel") # Initialize FastMCP server with app ID

# This function will now be the actual resource handler, decorated directly.
# It will be async and use httpx for the API call.
@mcp.tool()
async def get_hotel_metrics_resource() -> dict[str, Any]:
    """
    Handles requests for the hotel metrics resource.
    Fetches data from the GraphQL API using httpx.AsyncClient.
    FastMCP will automatically serialize the returned dictionary to JSON.
    """
    url = "https://zjmuqawoq5azfcndh7jjlrmroa.appsync-api.ap-south-1.amazonaws.com/graphql"

    headers = {
        "x-api-key": "da2-hpf5f2lxyjed7gha7rrxhfkguq",
        "Content-Type": "application/json"
    }

    query = """
    query GetHotelMetrics {
      getHotelMetrics(
        hotelId: "02497a43-5339-453a-9731-d14431a66070",
        startDate: "2025-04-28",
        endDate: "2025-07-02",
        fetchFromPostgres: true
      ) {
        hotelMetric {
          day
          formattedDate
          hotelId
          hotelName
          reportDate
          totalStats {
            adoptionRate
            checkIns {
              success
              failed
            }
            checkOuts {
              success
              failed
            }
            engagementRate
          }
        }
      }
    }
    """

    payload = {
        "query": query,
        "variables": {}
    }

    async with httpx.AsyncClient() as client: # Use async client for async function
        try:
            response = await client.post(url, json=payload, headers=headers)
            response.raise_for_status()
            return response.json()
        except httpx.RequestError as e:
            print(f"❌ HTTP request failed in get_hotel_metrics_resource: {e}")
            return {"error": str(e), "message": "Failed to retrieve hotel metrics from API."}
        except Exception as e:
            print(f"❌ Unexpected error in get_hotel_metrics_resource: {e}")
            return {"error": str(e), "message": "An unexpected error occurred."}

# The explicit JsonResource instantiation is removed.
# The resource is now registered via the @mcp.resource decorator.

if __name__ == "__main__":
    mcp.run(transport='stdio')