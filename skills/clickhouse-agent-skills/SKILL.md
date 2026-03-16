---
name: clickhouse-agent-skills
description: "The official Agent Skills for ClickHouse and ClickHouse Cloud"
homepage: https://github.com/ClickHouse/agent-skills
metadata:
  openclaw:
    emoji: "🤖"
    auto_generated: true
    requires:
      bins: ["npx", "skills"]
---

# Clickhouse Agent Skills

# ClickHouse Agent Skills

## Installation

```bash
npx skills add clickhouse/agent-skills
```

The CLI auto-detects installed agents and prompts you to select where to install.

## Usage

After installation, your AI agent will reference these best practices when:

- Creating new tables with `CREATE TABLE`
- Choosing `ORDER BY` / `PRIMARY KEY` columns
- Selecting data types for columns
- Optimizing slow queries
- Writing or tuning JOINs
- Designing data ingestion pipelines
- Handling updates or deletes

Example prompt:

> "Create a table for storing user events with fields for user_id, event_type, properties (JSON), and timestamp"

The agent will apply relevant rules like proper co
