---
name: aidenybai-react-grab
description: "Select context for coding agents directly from your website"
homepage: https://github.com/aidenybai/react-grab
metadata:
  openclaw:
    emoji: "🌐"
    auto_generated: true
    requires:
      bins: ["npm", "npx", "react-grab"]
---

# Aidenybai React Grab

# <img src="https://github.com/aidenybai/react-grab/blob/main/.github/public/logo.png?raw=true" width="60" align="center" /> React Grab

## Installation

Run this command at your project root (where `next.config.ts` or `vite.config.ts` is located):

```bash
npx -y grab@latest init
```

## Usage

Once installed, hover over any UI element in your browser and press:

- **⌘C** (Cmd+C) on Mac
- **Ctrl+C** on Windows/Linux

This copies the element's context (file name, React component, and HTML source code) to your clipboard ready to paste into your coding agent. For example:

```js
<a class="ml-auto inline-block text-sm" href="#">
  Forgot your password?
</a>
in LoginForm at components/login-form.tsx:46:19
```
