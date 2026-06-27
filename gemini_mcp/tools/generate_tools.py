"""Generate group: generate_text"""

import logging

from fastmcp import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field
from typing import Optional

from .. import service
from ..logging_utils import ToolLogger
from ..schemas import GeminiGenerateTextData, GeminiGenerateTextResult
from ._helpers import _err, _handle_request_exc, _upstream_err

logger = logging.getLogger("gemini-mcp.tools.generate")


def register_generate_tools(mcp: FastMCP) -> None:

    @mcp.tool(
        name="generate_text",
        description="Generate text using Gemini LLM",
        annotations=ToolAnnotations(readOnlyHint=False, destructiveHint=False, openWorldHint=True),
    )
    def generate_text(
        query: str = Field(
            ..., description="Required. Natural language prompt to send to Gemini. Any text is accepted; no length limit is enforced by this tool.",
        ),
        model: Optional[str] = Field(
            default="gemini-2.5-flash",
            description="Optional. Gemini model name, e.g., 'gemini-2.5-flash' or 'gemini-2.5-pro'. Defaults to 'gemini-2.5-flash'.",
        ),
    ) -> GeminiGenerateTextResult:
        tlog = ToolLogger(logger, "generate_text")

        body = {"contents": [{"parts": [{"text": query}]}]}

        try:
            data, status, retry_after = service.api_request(
                "POST", f"{model}:generateContent", body=body
            )
            if 200 <= status < 300:
                try:
                    text = data["candidates"][0]["content"]["parts"][0]["text"]
                except KeyError:
                    return _err(
                        GeminiGenerateTextResult, tlog,
                        "UPSTREAM_ERROR", "Unexpected response shape", 502
                    )
                tlog.success()
                return GeminiGenerateTextResult(
                    success=True,
                    statusCode=status,
                    data=GeminiGenerateTextData(prompt=query, response=text),
                )
            return _upstream_err(GeminiGenerateTextResult, tlog, status, data, retry_after)
        except Exception as exc:
            return _handle_request_exc(GeminiGenerateTextResult, tlog, exc)
