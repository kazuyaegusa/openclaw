---
name: taylorwilsdon-google-workspace-mcp
description: "Control Gmail, Google Calendar, Docs, Sheets, Slides, Chat, Forms, Tasks, Search & Drive with AI -"
homepage: https://github.com/taylorwilsdon/google_workspace_mcp
metadata:
  openclaw:
    emoji: "🔌"
    auto_generated: true
    requires:
      bins: ["docker", "git", "go", "jq"]
---

# Taylorwilsdon Google Workspace Mcp

<!-- mcp-name: io.github.taylorwilsdon/workspace-mcp -->

<div align="center">

## Usage

<details>
<summary><b>Quick Reference Card</b> - Essential commands & configs at a glance</summary>

<table>
<tr><td width="33%" valign="top">

**Credentials**

```bash
export GOOGLE_OAUTH_CLIENT_ID="..."
export GOOGLE_OAUTH_CLIENT_SECRET="..."
```

[Full setup →](#credential-configuration)

</td><td width="33%" valign="top">

**Launch Commands**

```bash
uvx workspace-mcp --tool-tier core
uv run main.py --tools gmail drive
```

[More options →](#start-the-server)

</td><td width="34%" valign="top">
