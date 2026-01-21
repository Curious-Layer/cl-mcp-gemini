import argparse
import requests
from fastmcp import FastMCP
from fastmcp.exceptions import ToolError


mcp = FastMCP("CL LLM Query MCP Server")


GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/models/"


@mcp.tool("gemini_ai_generate_text", description="Generate text using Gemini LLM")
def gemini_ai_generate_text(query: str, gemini_api_key: str, model: str = "gemini-2.5-flash"):
    headers = {"Content-Type": "application/json"}
    params = {"key": gemini_api_key}

    body = {
        "contents": [
            {
                "parts": [{"text": query}]
            }
        ]
    }

    try:
        response = requests.post(f"{GEMINI_BASE_URL}{model}:generateContent", headers=headers, params=params, json=body, timeout=20)
        # response.raise_for_status()
        data = response.json()
        print(data)
        text = data["candidates"][0]["content"]["parts"][0]["text"]
        return {"prompt": query, "response": text}

    except Exception as e:
        raise ToolError(status_code=500, detail=str(e))
    finally:
        # Clean up any resources if needed
        pass


def parse_args():
    parser = argparse.ArgumentParser(description="Run CL LLM Query MCP Server")
    parser.add_argument("-t", "--transport", help="Transport method for MCP (e.g. 'stdio', 'sse', or 'streamable-http')", default=None)
    parser.add_argument("--host", help="Host to bind the server to", default=None)
    parser.add_argument("--port", type=int, help="Port to bind the server to", default=None)
    return parser.parse_args()


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