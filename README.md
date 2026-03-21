# Gemini MCP Server

**Generate text using Google's Gemini LLM via API.**

A Model Context Protocol (MCP) server that exposes Google Gemini's API for generating text content.

---

## Overview

The Gemini MCP Server provides stateless, multi-user access to Gemini's core operations:

- **Text Generation** — Generate high-quality text using the Gemini LLM
- **Flexible Prompting** — Support for custom queries and model selection
- **API Integration** — Seamless integration with the Gemini API

Perfect for:

- Building AI-powered content generation workflows
- Automating text creation tasks
- Integrating LLM capabilities into multi-agent systems

---

## Tools

<details>
<summary><code>gemini_ai_generate_text</code> — Generate text using Gemini LLM</summary>

**Inputs:**

- `query` (string, required) — The prompt or question to send to Gemini
- `gemini_api_key` (string, required) — Valid Google Gemini API key
- `model` (string, optional) — Model to use for generation (default: "gemini-2.5-flash")

**Output:**

```json
{
  "prompt": "Your original query",
  "response": "Generated text response from Gemini"
}
```

**Usage Example:**

```bash
POST /mcp/cl-llm-query/gemini_ai_generate_text

{
  "query": "Write a short story about a robot learning to paint",
  "gemini_api_key": "AIzaSyDxxxxxxxxxxxxxxxxxxxxxx",
  "model": "gemini-2.5-flash"
}
```

</details>

---

<details>
<summary><strong>API Parameters Reference</strong></summary>

### Model Selection

- `model` — Specifies which Gemini model to use (default: "gemini-2.5-flash")

### Available Models

**Gemini Models:**

```
gemini-2.5-flash — Fast, efficient model for quick text generation
gemini-2.0-pro — Advanced model for complex queries
gemini-1.5-pro — Standard pro model
```

</details>

---

<details>
<summary><strong>API Key Referance</strong></summary>

All tools require a valid Google Gemini API key. Here's how to obtain one:

### Step 1: Create Google Cloud Project

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable the **Gemini API** from the API Library

### Step 2: Create API Credentials

1. Navigate to **Credentials** in Google Cloud Console
2. Click **+ Create Credentials** → **API Key**
3. Copy the generated API key

### Step 3: Authenticate

Use your API key in the `gemini_api_key` parameter for each request.

Refer to [Google Gemini API Documentation](https://ai.google.dev/docs) for detailed setup steps.

### Step 4: Required Scopes

Ensure your API key has access to:

- `generativelanguage.googleapis.com` — Text generation API

</details>

---

<details>
<summary><strong>Troubleshooting</strong></summary>

### **Missing or Invalid API Key**

- **Cause:** API key not provided in request or incorrect format
- **Solution:**
  1. Verify `gemini_api_key` parameter is present in request
  2. Check API key is active in your Google Cloud account
  3. Regenerate API key if expired

### **Insufficient Credits**

- **Cause:** API calls have exceeded your requests limits
- **Solution:**
  1. Check credit usage in your Curious Layer dashboard
  2. Upgrade to a paid plan or add credits for higher limits
  3. Contact support for credit adjustments

### **Malformed Request Payload**

- **Cause:** JSON payload is invalid or missing required fields
- **Solution:**
  1. Validate JSON syntax before sending
  2. Ensure all required parameters (`query`, `gemini_api_key`) are included
  3. Check parameter types match expected values (string)

### **Server Not Found**

- **Cause:** Incorrect server name in the API endpoint
- **Solution:**
  1. Verify endpoint format: `/mcp/{server-name}/{tool-name}`
  2. Use lowercase server name: `/mcp/cl-llm-query/...`
  3. Check available servers in documentation

### **API Key Invalid or Expired**

- **Cause:** API key rejected by Google or has expired
- **Solution:**
  1. Generate a fresh API key from Google Cloud Console
  2. Verify API key has Gemini API enabled
  3. Check key expiration and regenerate if needed

</details>

---

<details>
<summary><strong>Resources</strong></summary>

- **[Google Gemini API](https://aistudio.google.com/api-keys)** — Official Gen AI API reference
- **[Google Cloud Console](https://console.cloud.google.com/)** — Credentials management
- **[Gemini API Reference](https://ai.google.dev/api)** — Complete Gemini API endpoint reference
- **[Model Context Protocol Docs](https://modelcontextprotocol.io/)** — MCP specification

</details>

---