import requests
from fastmcp import FastMCP
from fastmcp.exceptions import ToolError

from .config import GEMINI_BASE_URL
from .schemas import GeminiGenerateTextResponse


def register_tools(mcp: FastMCP) -> None:
    @mcp.tool("gemini_ai_generate_text", description="Generate text using Gemini LLM")
    def gemini_ai_generate_text(
        query: str,
        gemini_api_key: str,
        model: str = "gemini-2.5-flash",
    ) -> GeminiGenerateTextResponse:
        headers = {"Content-Type": "application/json"}
        params = {"key": gemini_api_key}

        body = {"contents": [{"parts": [{"text": query}]}]}

        try:
            response = requests.post(
                f"{GEMINI_BASE_URL}{model}:generateContent",
                headers=headers,
                params=params,
                json=body,
                timeout=20,
            )
            data = response.json()
            print(data)
            text = data["candidates"][0]["content"]["parts"][0]["text"]
            return {"prompt": query, "response": text}

        except Exception as e:
            raise ToolError(str(e))
        finally:
            pass
