def processDataMCP():
    response = sendReq()

    if response.status_code == 200:
        try:
            data = response.json()
            hotel_metrics = data["data"]["getHotelMetrics"]["hotelMetric"]

            # Format into MCP context structure
            mcp_context = {
                "context": [
                    {
                        "name": "hotel_metrics_summary",
                        "type": "structured",
                        "data": []
                    }
                ]
            }

            for entry in hotel_metrics:
                metric_entry = {
                    "day": entry.get("day"),
                    "hotelName": entry.get("hotelName"),
                    "mobileApp": entry.get("channelCheckInBreakDown", {}).get("mobileApp"),
                    "kiosk": entry.get("channelCheckInBreakDown", {}).get("kiosk"),
                    "conversionRate": entry.get("totalStats", {}).get("conversionRate")
                }
                mcp_context["context"][0]["data"].append(metric_entry)

            # 🧠 You can return this dict to the MCP consumer
            return mcp_context

        except Exception as e:
            print("❌ Error while parsing response:", e)
            return {}
    else:
        print("❌ Request failed. Status code:", response.status_code)
        return {}
context_data = processDataMCP()
print(json.dumps(context_data, indent=2))  # Optional: view it



