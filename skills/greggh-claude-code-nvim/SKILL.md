---
name: greggh-claude-code-nvim
description: "Seamless integration between Claude Code AI assistant and Neovim"
homepage: https://github.com/greggh/claude-code.nvim
metadata:
  openclaw:
    emoji: "🤖"
    auto_generated: true
    requires:
      bins: ["git"]
---

# Greggh Claude Code Nvim

# Claude Code Neovim Plugin

## Usage

```vim
" In your Vim/Neovim commands or init file:
:ClaudeCode
```

```lua
-- Or from Lua:
vim.cmd[[ClaudeCode]]

-- Or map to a key:
vim.keymap.set('n', '<leader>cc', '<cmd>ClaudeCode<CR>', { desc = 'Toggle Claude Code' })
```
