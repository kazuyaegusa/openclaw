---
name: shareai-lab-learn-claude-code
description: "Bash is all You need - Write a nano Claude Code 0 - 1"
homepage: https://github.com/shareAI-lab/learn-claude-code
metadata:
  openclaw:
    emoji: "🤖"
    auto_generated: true
    requires:
      bins: ["git", "npm", "pip"]
---

# Shareai Lab Learn Claude Code

[English](./README.md) | [中文](./README-zh.md) | [日本語](./README-ja.md)

## Usage

```sh
git clone https://github.com/shareAI-lab/learn-claude-code
cd learn-claude-code
pip install -r requirements.txt
cp .env.example .env   # Edit .env with your ANTHROPIC_API_KEY

python agents/s01_agent_loop.py       # Start here
python agents/s12_worktree_task_isolation.py  # Full progression endpoint
python agents/s_full.py               # Capstone: all mechanisms combined
```
