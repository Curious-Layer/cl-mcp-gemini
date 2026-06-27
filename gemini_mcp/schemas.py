from pydantic import BaseModel, ConfigDict
from typing import Any


class ToolError(BaseModel):
    code: str
    message: str
    details: Any = None


class ToolResult(BaseModel):
    success: bool
    statusCode: int
    retriable: bool = False
    retry_after_seconds: int | None = None
    error: ToolError | None = None


class GeminiGenerateTextData(BaseModel):
    model_config = ConfigDict(extra="allow")

    prompt: str
    response: str


class GeminiGenerateTextResult(ToolResult):
    data: GeminiGenerateTextData | None = None
