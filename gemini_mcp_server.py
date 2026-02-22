from fastmcp import FastMCP
from gemini_mcp.cli import parse_args
from gemini_mcp.tools import register_tools


mcp = FastMCP("CL LLM Query MCP Server")
register_tools(mcp)


if __name__ == "__main__":
    args = parse_args()

    # Build kwargs for mcp.run() only with provided values
    run_kwargs = {}
    if args.transport:
        run_kwargs["transport"] = args.transport
    if args.host:
        run_kwargs["host"] = args.host
    if args.port:
        run_kwargs["port"] = args.port

    # Start the MCP server with optional transport/host/port
    mcp.run(**run_kwargs)