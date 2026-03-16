---
name: promptfoo-promptfoo
description: "Test your prompts, agents, and RAGs. AI Red teaming, pentesting, and vulnerability scanning for"
homepage: https://github.com/promptfoo/promptfoo
metadata:
  openclaw:
    emoji: "📦"
    auto_generated: true
    requires:
      bins: ["npm", "npx", "pip", "promptfoo"]
---

# Promptfoo Promptfoo

# Promptfoo: LLM evals & red teaming

## Usage

```sh
npm install -g promptfoo
promptfoo init --example getting-started
```

Also available via `brew install promptfoo` and `pip install promptfoo`. You can also use `npx promptfoo@latest` to run any command without installing.

Most LLM providers require an API key. Set yours as an environment variable:

```sh
export OPENAI_API_KEY=sk-abc123
```

Once you're in the example directory, run an eval and view results:

```sh
cd getting-started
promptfoo eval
promptfoo view
```

See [Getting Started
