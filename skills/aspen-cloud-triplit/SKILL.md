---
name: aspen-cloud-triplit
description: "A full-stack, syncing database that runs on both server and client. Pluggable storage (indexeddb,"
homepage: https://github.com/aspen-cloud/triplit
metadata:
  openclaw:
    emoji: "🌐"
    auto_generated: true
    requires:
      bins: ["npm"]
---

# Aspen Cloud Triplit

![Triplit banner](https://www.triplit.dev/opengraph-image.png)

## Usage

Start a new project.

```bash
npm create triplit-app@latest my-app
```

Or add the dependencies to an existing project.

```bash
npm install --save-dev @triplit/cli
npm run triplit init
```

Define a [schema](https://www.triplit.dev/docs/schemas) in `my-app/triplit/schema.ts`.

```ts
import { Schema as S, ClientSchema } from '@triplit/client';

export const schema = {
  todos: {
    schema: S.Schema({
      id: S.Id(),
      text: S.String(),
      completed: S.Boolean({ default: false }),
    }

```
