---
name: jredeker-opencode-morph-fast-apply
description: "OpenCode plugin for Morph Fast Apply - 10x faster code editing with lazy edit markers. No MCP"
homepage: https://github.com/JRedeker/opencode-morph-fast-apply
metadata:
  openclaw:
    emoji: "🔌"
    auto_generated: true
---

# Jredeker Opencode Morph Fast Apply

# opencode-morph-fast-apply

## Usage

The LLM uses `morph_edit` for efficient partial file edits:

```
morph_edit({
  target_filepath: "src/auth.ts",
  instructions: "I am adding error handling for invalid tokens",
  code_edit: `// ... existing code ...
function validateToken(token) {
  if (!token) {
    throw new Error("Token is required");
  }
  // ... existing code ...
}
// ... existing code ...`
})
```
