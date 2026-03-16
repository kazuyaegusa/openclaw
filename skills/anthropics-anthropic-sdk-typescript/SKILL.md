---
name: anthropics-anthropic-sdk-typescript
description: "Access to Anthropic's safety-first language model APIs in TypeScript"
homepage: https://github.com/anthropics/anthropic-sdk-typescript
metadata:
  openclaw:
    emoji: "🔧"
    auto_generated: true
    requires:
      bins: ["npm", "sdk"]
---

# Anthropics Anthropic Sdk Typescript

# <img src=".github/logo.svg" alt="" width="32"> Claude SDK for TypeScript

## Installation

```sh
npm install @anthropic-ai/sdk
```

## Usage

<!-- prettier-ignore -->
```js
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

const message = await client.messages.create({
  max_tokens: 1024,
  messages: [{ role: 'user', content: 'Hello, Claude' }],
  model: 'claude-sonnet-4-5-20250929',
});

console.log(message.content);
```
