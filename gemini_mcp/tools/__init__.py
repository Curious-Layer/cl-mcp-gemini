"""MewCP Gemini tool registration."""

from fastmcp import FastMCP

from .generate_tools import register_generate_tools


def register_tools(mcp: FastMCP) -> None:
    register_generate_tools(mcp)
