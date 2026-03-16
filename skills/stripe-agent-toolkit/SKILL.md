---
name: stripe-agent-toolkit
description: "One-stop shop for building AI-powered products and businesses with Stripe."
homepage: https://github.com/stripe/ai
metadata:
  openclaw:
    emoji: "🔧"
    auto_generated: true
    requires:
      bins: ["agent-toolkit", "npm", "npx", "pip", "stripe-agent-toolkit"]
---

# Stripe Agent Toolkit

![Hero GIF](https://stripe.dev/images/badges/ai-banner.gif)

## Installation

You don't need this source code unless you want to modify the package. If you just
want to use the package run:

```sh
pip install stripe-agent-toolkit
```

## Usage

The library needs to be configured with your account's secret key which is
available in your [Stripe Dashboard][api-keys]. We strongly recommend using a [Restricted API Key][restricted-keys] (`rk_*`) for better security and granular permissions. Tool availability is determined by the permissions you configure on the restricted key.

```python
from stripe_agent_toolkit.openai.toolkit import create_stripe_agent_toolkit

async def main():
    toolkit = await create_stripe_agent_toolkit(secret_key="

```
