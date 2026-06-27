**Access Google's most capable AI models through a single MCP tool.**

A Model Context Protocol (MCP) server that exposes Google Gemini's API for generating text using state-of-the-art large language models.


## Overview

The mewcp-gemini MCP Server provides direct access to Google's Gemini LLMs:

- Generate high-quality text responses from natural language prompts
- Choose between fast and capable Gemini model variants
- Integrate Gemini's reasoning into any MCP-compatible AI workflow

Perfect for:

- AI agents that need to delegate subtasks to a powerful LLM
- Generating summaries, translations, code, or creative content
- Augmenting workflows with Gemini's reasoning and language capabilities


## Tools


<details>
<summary><code>generate_text</code> — Generate text using Gemini LLM</summary>

Generate text using Gemini LLM

**Inputs:**
```
- `query` (string, required) — Required. Natural language prompt to send to Gemini. Any text is accepted; no length limit is enforced by this tool.
- `model` (string, optional, default: gemini-2.5-flash) — Optional. Gemini model name, e.g., 'gemini-2.5-flash' or 'gemini-2.5-pro'. Defaults to 'gemini-2.5-flash'.
```

**Output `data` schema:**

```typescript
{
  prompt: string;
  response: string;
}
```

</details>


## API Parameters Reference

<details>
<summary><strong>Response Envelope</strong></summary>

Every tool returns the same top-level envelope. Only `data` varies per tool.

```json
// Success
{
  "success": true,
  "statusCode": 200,
  "retriable": false,
  "retry_after_seconds": null,
  "error": null,
  "data": { ... }
}

// Error
{
  "success": false,
  "statusCode": 400,
  "retriable": false,
  "retry_after_seconds": null,
  "error": { "code": "{ERROR_CODE}", "message": "{description}", "details": {} },
  "data": null
}
```

- `retriable` — `true` when it is safe to retry (rate limit, network error, 503). `false` for validation and auth errors.
- `retry_after_seconds` — seconds to wait before retrying; present only when `retriable` is `true` and the upstream specifies a delay.
- `error.code` — machine-readable string: `VALIDATION_ERROR`, `AUTH_ERROR`, `UPSTREAM_ERROR`, `SERVER_ERROR`.

</details>


## Getting Your Gemini API Key

<details>
<summary><strong>Steps</strong></summary>

1. Go to [Google AI Studio API Keys](https://aistudio.google.com/app/apikey)
2. Sign in with your Google account and navigate to the API keys section
3. Click **Create API Key**
4. Copy the generated key — you will only see it once

</details>


## Troubleshooting

<details>
<summary><strong>Missing or Invalid Headers</strong></summary>

- **Cause:** API key not provided in request headers or incorrect format
- **Solution:**
  1. Verify `Authorization: Bearer YOUR_API_KEY` and `X-Mewcp-Credential-Id: CREDENTIAL-ID` headers are present
  2. Check API key is active in your MewCP account

</details>

<details>
<summary><strong>Insufficient Credits</strong></summary>

- **Cause:** API calls have exceeded your request limits
- **Solution:**
  1. Check credit usage in your Curious Layer dashboard
  2. Upgrade to a paid plan or add credits for higher limits
  3. Contact support for credit adjustments

</details>

<details>
<summary><strong>Credential Not Connected</strong></summary>

- **Cause:** No Gemini credential linked to your account
- **Solution:**
  1. Go to **Credentials** in your MewCP dashboard
  2. Add your API key (static)
  3. Retry the request with the correct `X-Mewcp-Credential-Id` header

</details>

<details>
<summary><strong>Malformed Request Payload</strong></summary>

- **Cause:** JSON payload is invalid or missing required fields
- **Solution:**
  1. Validate JSON syntax before sending
  2. Ensure all required tool parameters are included
  3. Check parameter types match expected values

</details>

<details>
<summary><strong>Server Not Found</strong></summary>

- **Cause:** Incorrect server name in the API endpoint
- **Solution:**
  1. Verify endpoint format: `mewcp-gemini/mcp/generate_text`
  2. Use correct server name from documentation
  3. Check available servers in your Curious Layer account

</details>

<details>
<summary><strong>Gemini API Error</strong></summary>

- **Cause:** Upstream Gemini API returned an error
- **Solution:**
  1. Check Gemini service status at [Google Status Page](https://status.cloud.google.com)
  2. Verify your credential has the required permissions
  3. Review the error message for specific details

</details>

---

<details>
<summary><strong>Resources</strong></summary>

- **[Gemini API Documentation](https://ai.google.dev/gemini-api/docs)** — Official API reference
- **[Gemini API Reference](https://ai.google.dev/api)** — Complete endpoint reference
- **[FastMCP Docs](https://gofastmcp.com/v2/getting-started/welcome)** — FastMCP specification
- **[FastMCP Credentials](https://pypi.org/project/fastmcp-credentials/)** — FastMCP Credentials package for credential handling


</details>
