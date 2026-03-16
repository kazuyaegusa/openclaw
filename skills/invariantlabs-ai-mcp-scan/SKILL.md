---
name: invariantlabs-ai-mcp-scan
description: "Security scanner for AI agents, MCP servers and agent skills."
homepage: https://github.com/invariantlabs-ai/mcp-scan
metadata:
  openclaw:
    emoji: "🔌"
    auto_generated: true
    requires:
      bins: ["git", "pip"]
---

# Invariantlabs Ai Mcp Scan

<p align="center">
  <h1 align="center">
  Snyk Agent Scan
  </h1>
</p>

<p align="center">
  Discover and scan agent components on your machine for prompt injections<br/>
  and vulnerabilities (including agents, MCP servers, skills).
</p>

> **NEW** Read our [technical report on the emerging threats of the agent skill eco-system](.github/reports/skills-report.pdf) published together with Agent Scan 0.4, which adds support for scanning agent skills.

<p align="center">
  <a href="https://pypi.py

## Usage

To get started:

1. **Sign up at [Snyk](https://snyk.io)** and get an API token from [https://app.snyk.io/account](https://app.snyk.io/account) (API Token → KEY → click to show).
2. **Set the token as an environment variable** before running any scan:
   ```bash
   export SNYK_TOKEN=your-api-token-here
   ```
3. Have [uv](https://docs.astral.sh/uv/getting-started/installation/) installed on your system.
