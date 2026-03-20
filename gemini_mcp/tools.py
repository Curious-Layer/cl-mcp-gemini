import requests
from fastmcp import FastMCP
from fastmcp.exceptions import ToolError
from pydantic import Field
from .config import GEMINI_BASE_URL
from .schemas import GeminiGenerateTextResponse
from typing import Optional


def register_tools(mcp: FastMCP) -> None:
    @mcp.tool("gemini_ai_generate_text", description="Generate text using Gemini LLM")
    def gemini_ai_generate_text(
        query: str = Field(..., description="Natural language prompt to send to Gemini."),
        gemini_api_key: str = Field(..., description="Google Gemini API key."),
        model: Optional[str] = Field(default= "gemini-2.5-flash", description="Gemini model name, e.g., 'gemini-2.5-flash' or 'gemini-2.5-pro'."),
    ) -> GeminiGenerateTextResponse:
        """
        Returns:
            A dictionary containing the original prompt and generated text response.
        """
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
