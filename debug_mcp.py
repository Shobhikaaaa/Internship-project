from mcp.server.fastmcp import FastMCP

mcp = FastMCP("hotel")

@mcp.tool()
async def ping():
    print("✅ tool ping registered!")
    return {"message": "pong"}

if __name__ == "__main__":
    print("🚀 STARTING DEBUG MCP")
    mcp.run(transport="stdio")
