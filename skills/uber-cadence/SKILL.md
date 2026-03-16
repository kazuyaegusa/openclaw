---
name: uber-cadence
description: "Cadence is a distributed, scalable, durable, and highly available orchestration engine to execute"
homepage: https://github.com/cadence-workflow/cadence
metadata:
  openclaw:
    emoji: "🗄️"
    auto_generated: true
    requires:
      bins: ["cadence-workflow", "docker", "git"]
---

# Uber Cadence

# Cadence

[![Build Status](https://github.com/cadence-workflow/cadence/actions/workflows/ci-checks.yml/badge.svg)](https://github.com/cadence-workflow/cadence/actions/workflows/ci-checks.yml)
[![Coverage](https://codecov.io/gh/cadence-workflow/cadence/graph/badge.svg?token=7SD244ImNF)](https://codecov.io/gh/cadence-workflow/cadence)
[![Slack Status](https://img.shields.io/badge/slack-join_chat-white.svg?logo=slack&style=social)](https://communityinviter.com/apps/cloud-native/cncf)
[![Github rele

## Installation

Cadence backend consists of multiple services, a database (Cassandra/MySQL/PostgreSQL) and optionally Kafka+Elasticsearch.
As a user, you need a worker which contains your workflow implementation.
Once you have Cadence backend and worker(s) running, you can trigger workflows by using SDKs or via CLI.

1. Start cadence backend components locally

```
docker compose -f docker/docker-compose.yml up
```

2. Run the Samples

Try out the sample recipes for [Go](https://github.com/cadence-workflow/cade
