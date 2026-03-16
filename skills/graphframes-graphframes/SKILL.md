---
name: graphframes-graphframes
description: "GraphFrames is a package for Apache Spark which provides DataFrame-based Graphs"
homepage: https://github.com/graphframes/graphframes
metadata:
  openclaw:
    emoji: "🔧"
    auto_generated: true
---

# Graphframes Graphframes

<p align="center">
    <img src="docs/src/img/GraphFrames-Logo-Large.png" alt="GraphFrames Logo" width="500"/>
</p>

<p align="center">
    <a href="https://github.com/graphframes/graphframes/actions/workflows/scala-ci.yml"><img src="https://github.com/graphframes/graphframes/actions/workflows/scala-ci.yml/badge.svg" alt="Scala CI"></a> <a href="https://github.com/graphframes/graphframes/actions/workflows/python-ci.yml"><img src="https://github.com/graphframes/graphframes/actions/workflows/pytho

## Usage

Now you can create a GraphFrame as follows.

```python
from pyspark.sql import SparkSession
from graphframes import GraphFrame

spark = SparkSession.builder.getOrCreate()

nodes = [
    (1, "Alice", 30),
    (2, "Bob", 25),
    (3, "Charlie", 35)
]
nodes_df = spark.createDataFrame(nodes, ["id", "name", "age"])

edges = [
    (1, 2, "friend"),
    (2, 1, "friend"),
    (2, 3, "friend"),
    (3, 2, "enemy")  # eek!
]
edges_df = spark.createDataFrame(edges, ["src", "dst", "relationship"])

g = Grap

```
