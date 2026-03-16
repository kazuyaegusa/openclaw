---
name: u14app-deep-research
description: "Use any LLMs (Large Language Models) for Deep Research. Support SSE API and MCP server."
homepage: https://github.com/u14app/deep-research
metadata:
  openclaw:
    emoji: "🔌"
    auto_generated: true
    requires:
      bins: ["docker", "git", "npm", "or"]
---

# U14app Deep Research

<div align="center">
<h1>Deep Research</h1>

![GitHub deployments](https://img.shields.io/github/deployments/u14app/gemini-next-chat/Production)
![GitHub Release](https://img.shields.io/github/v/release/u14app/deep-research)
![Docker Image Size](https://img.shields.io/docker/image-size/xiangfa/deep-research/latest)
![Docker Pulls](https://img.shields.io/docker/pulls/xiangfa/deep-research)
[![License: MIT](https://img.shields.io/badge/License-MIT-default.svg)](https://opensource.org/licenses/MIT)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/u14app/deep-research.git
   cd deep-research
   ```

2. **Install dependencies:**

   ```bash
   pnpm install  # or npm install or yarn install
   ```

3. **Set up Environment Variables:**

   You need to modify the file `env.tpl` to `.env`, or create a `.env` file and write the variables to this file.

   ```bash
   # For Development
   cp env.tpl .env.local
   # For Production
   cp env.tpl .env
   ```

4. \*\*Run the devel
