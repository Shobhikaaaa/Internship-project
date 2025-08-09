
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("mcp-server")

@mcp.tool()
def get_checkin_summary() -> str:
    return "This tool summarizes check-in data."

if __name__ == "__main__":
    mcp.run(transport="stdio")
