---
name: coder-claudecode-nvim
description: "🧩 Claude Code Neovim IDE Extension"
homepage: https://github.com/coder/claudecode.nvim
metadata:
  openclaw:
    emoji: "🤖"
    auto_generated: true
    requires:
      bins: ["curl", "git", "npm"]
---

# Coder Claudecode Nvim

# claudecode.nvim

## Installation

```lua
{
  "coder/claudecode.nvim",
  dependencies = { "folke/snacks.nvim" },
  config = true,
  keys = {
    { "<leader>a", nil, desc = "AI/Claude Code" },
    { "<leader>ac", "<cmd>ClaudeCode<cr>", desc = "Toggle Claude" },
    { "<leader>af", "<cmd>ClaudeCodeFocus<cr>", desc = "Focus Claude" },
    { "<leader>ar", "<cmd>ClaudeCode --resume<cr>", desc = "Resume Claude" },
    { "<leader>aC", "<cmd>ClaudeCode --continue<cr>", desc = "Continue Claude" },
    { "<leader>am", "<cmd>ClaudeCodeSelec



## Usage

1. **Launch Claude**: Run `:ClaudeCode` to open Claude in a split terminal
2. **Send context**:
   - Select text in visual mode and use `<leader>as` to send it to Claude
   - In `nvim-tree`/`neo-tree`/`oil.nvim`/`mini.nvim`, press `<leader>as` on a file to add it to Claude's context
3. **Let Claude work**: Claude can now:
   - See your current file and selections in real-time
   - Open files in your editor
   - Show diffs with proposed changes
   - Access diagnostics and workspace info

```
