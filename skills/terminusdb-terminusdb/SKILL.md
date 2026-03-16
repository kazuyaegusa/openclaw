---
name: terminusdb-terminusdb
description: "TerminusDB is a distributed, collaborative database designed for building, sharing, versioning, and"
homepage: https://github.com/terminusdb/terminusdb
metadata:
  openclaw:
    emoji: "🗄️"
    auto_generated: true
    requires:
      bins: ["docker", "git", "mocha", "npx"]
---

# Terminusdb Terminusdb

<img
  src="https://github.com/terminusdb/terminusdb-web-assets/blob/master/readmes/terminusdb/TerminusDB-Logo-Colour_3.png"
  alt="TerminusDB Logo"
  width="30%"
  align="center"
/>

---

[![Native Build](https://github.com/terminusdb/terminusdb/actions/workflows/native-build.yml/badge.svg?branch=main&event=push)](https://github.com/terminusdb/terminusdb/actions/workflows/native-build.yml)
[![Docker Build](https://github.com/terminusdb/terminusdb/actions/workflows/docker-images-publish.yml/badg

## Installation

The easiest way to install TerminusDB as a developer is by using the [Docker TerminusDB Image](https://hub.docker.com/r/terminusdb/terminusdb-server). It can be joined by using [Snap](https://snapcraft.io/terminusdb) locally as a git-for-data client to perform push and pull. Docker brings the server component, and snap the ability to try TerminusDB on the command line, for example for ML/Ops.

For deployments, copy the docker-compose.yml file from the repository. For a complete modeller user in
