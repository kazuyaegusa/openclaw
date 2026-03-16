---
name: pgvector-pgvector
description: "Open-source vector similarity search for Postgres"
homepage: https://github.com/pgvector/pgvector
metadata:
  openclaw:
    emoji: "🗄️"
    auto_generated: true
    requires:
      bins: ["docker", "git", "pgvector"]
---

# Pgvector Pgvector

# pgvector

## Installation

Enable the extension (do this once in each database where you want to use it)

```tsql
CREATE EXTENSION vector;
```

Create a vector column with 3 dimensions

```sql
CREATE TABLE items (id bigserial PRIMARY KEY, embedding vector(3));
```

Insert vectors

```sql
INSERT INTO items (embedding) VALUES ('[1,2,3]'), ('[4,5,6]');
```

Get the nearest neighbors by L2 distance

```sql
SELECT * FROM items ORDER BY embedding <-> '[3,1,2]' LIMIT 5;
```

Also supports inner product (`<#>`), cosine distance (
