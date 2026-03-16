---
name: milanglacier-minuet-ai-nvim
description: "💃 Dance with Intelligence in Your Code. Minuet offers code completion as-you-type from popular LLMs"
homepage: https://github.com/milanglacier/minuet-ai.nvim
metadata:
  openclaw:
    emoji: "🔧"
    auto_generated: true
    requires:
      bins: ["curl", "git"]
---

# Milanglacier Minuet Ai Nvim

- [Minuet](#minuet)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Quick Start](#quick-start)
  - [Virtual Text Setup](#virtual-text-setup)
  - [Nvim-cmp setup](#nvim-cmp-setup)
  - [Blink-cmp Setup](#blink-cmp-setup)
  - [Built-in Completion, Mini.Completion, and LSP Setup](#built-in-completion-minicompletion-and-lsp-setup)
  - [LLM Provider Examples](#llm-provider-examples)
    - [Openrouter Kimi-K2](#openrouter-kimi-k2)
    - [Deepseek](#deepseek)

## Installation

**Lazy.nvim**:

```lua
specs = {
    {
        'milanglacier/minuet-ai.nvim',
        config = function()
            require('minuet').setup {
                -- Your configuration options here
            }
        end,
    },
    { 'nvim-lua/plenary.nvim' },
    -- optional, if you are using virtual-text frontend, nvim-cmp is not
    -- required.
    { 'hrsh7th/nvim-cmp' },
    -- optional, if you are using virtual-text frontend, blink is not required.
    { 'Saghen/blink.cmp' },
}
```

\*\*Roc
