---
name: metorial-metorial
description: "Connect any AI model to 600+ integrations; powered by MCP 📡 🚀"
homepage: https://github.com/metorial/metorial
metadata:
  openclaw:
    emoji: "🔧"
    auto_generated: true
    requires:
      bins: ["go"]
---

# Metorial Metorial

<img src="./assets/repo-header.webp" alt="Metorial" width="100%" />

<br />

<h1 align="center">Metorial (YC F25)</h1>

<p align="center">
The open source integration platform for agentic AI. <br />
Connect any AI model to thousands of APIs, data sources, and tools with a single function call.
</p>

> [!TIP]
> _Skip the setup and go hosted:_ The fasted, simplest and most reliable way to use [Metorial](https://metorial.com) is to sign up to [our hosted platform](https://app.metorial.com/).
>
> ➡

## Usage

The simplest way to get started is with the `.run()` method, which handles session management and conversation loops automatically:

```typescript
import { Metorial } from 'metorial';
import OpenAI from 'openai';

let metorial = new Metorial({ apiKey: 'your-metorial-api-key' });
let openai = new OpenAI({ apiKey: 'your-openai-api-key' });

let result = await metorial.run({
  message: 'Scan my slack messages for meetings and put them on my google calendar.',
  serverDeployments: ['google-calendar-

```
