---
name: rohitg00-skillkit
description: "Supercharge AI coding agents with portable skills. Install, translate & share skills across Claude"
homepage: https://github.com/rohitg00/skillkit
metadata:
  openclaw:
    emoji: "🤖"
    auto_generated: true
    requires:
      bins: ["curl", "git", "npm", "npx", "pip", "skillkit", "skillkit-client"]
---

# Rohitg00 Skillkit

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/img/banner.svg">
  <source media="(prefers-color-scheme: light)" srcset="docs/img/banner.svg">
  <img alt="SkillKit - One Skill. Every Agent." src="docs/img/banner.svg" width="100%">
</picture>

<br/>
<br/>

[![CI](https://github.com/rohitg00/skillkit/actions/workflows/ci.yml/badge.svg)](https://github.com/rohitg00/skillkit/actions/workflows/ci.yml)
[![npm version](https://img.shields.io/npm/v/skillkit.sv

## Installation

```bash
npm install -g skillkit       # npm
pnpm add -g skillkit          # pnpm
yarn global add skillkit      # yarn
bun add -g skillkit           # bun
npx skillkit <command>        # no install
```

## Usage

```bash
npx skillkit@latest init              # Detect agents, create dirs
skillkit recommend                    # Get smart suggestions
skillkit install anthropics/skills    # Install from marketplace
skillkit sync                         # Deploy to your agents
```

Four commands. Your agents now have skills for PDF processing, code review, and more.
