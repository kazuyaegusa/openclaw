---
name: alibaba-pipcook
description: "Machine learning platform for Web developers"
homepage: https://github.com/alibaba/pipcook
metadata:
  openclaw:
    emoji: "🧠"
    auto_generated: true
    requires:
      bins: ["cli", "docker", "git", "npm"]
---

# Alibaba Pipcook

<p align="center">
  <a href="https://alibaba.github.io/pipcook/">
    <img alt="pipcook" src="./docs/images/logo.png" width="160">
  </a>
</p>

<p align="center">
  A JavaScript application framework for machine learning and its engineering.
</p>

<p align="center">
  <a href="https://www.npmjs.com/package/@pipcook/core">
    <img alt="npm" src="https://img.shields.io/npm/v/@pipcook/core"></a>
  <a href="https://www.npmjs.com/package/@pipcook/core">
    <img alt="npm" src="https://img.shields.i

## Installation

Prepare the following on your machine:

| Installer   | Version Range         |
| ----------- | --------------------- |
| [Node.js][] | >= 12.17 or >= 14.0.0 |
| [npm][]     | >= 6.14.4             |

Install the command-line tool for managing [Pipcook][] projects:

```shell
$ npm install -g @pipcook/cli
```

Then train from anyone of those [pipelines](./example/pipelines/), we take image classification as an example:

```shell
$ pipcook train https://cdn.jsdelivr.net/gh/alibaba/pipcook@main/example/pipelines/image-cl



```
