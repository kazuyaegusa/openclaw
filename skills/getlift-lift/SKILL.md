---
name: getlift-lift
description: "Expanding Serverless Framework beyond functions using the AWS CDK"
homepage: https://github.com/getlift/lift
metadata:
  openclaw:
    emoji: "📦"
    auto_generated: true
    requires:
      bins: ["npm"]
---

# Getlift Lift

![](docs/img/animation.gif)

Lift is a plugin that leverages the AWS CDK to expand the [Serverless Framework](https://github.com/oss-serverless/serverless) beyond functions.

Deploy production-ready websites, queues, storage buckets and more with a few lines in serverless.yml.

- ⚡️ **For developers** - No AWS knowledge required
- ⚡️ **Production-ready** - Built by AWS experts, optimized for production
- ⚡️ **Not invasive** - Integrates with existing projects
- ⚡️ **No lock-in** - Eject to Cloud

## Installation

Lift is a [Serverless Framework plugin](https://www.serverless.com/plugins/), install it in your project:

```bash
serverless plugin install -n serverless-lift
```

> If you prefer, you can install Lift via NPM: `npm install --save-dev serverless-lift`. Then, register the `serverless-lift` plugin in `serverless.yml` (see the example below).

## Usage

Once installed, start using Lift constructs in `serverless.yml`:

```yaml
service: my-app

provider:
  name: aws

plugins:
  - serverless-lift

functions:
  # ...

constructs:
  # Include Lift constructs here

  landing-page:
    type: static-website
    path: "landing/dist"

  avatars:
    type: storage
```
