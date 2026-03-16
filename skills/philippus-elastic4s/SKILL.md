---
name: philippus-elastic4s
description: "🔍 Elasticsearch Scala Client - Reactive, Non Blocking, Type Safe, HTTP Client"
homepage: https://github.com/Philippus/elastic4s
metadata:
  openclaw:
    emoji: "🌐"
    auto_generated: true
    requires:
      bins: ["docker", "node"]
---

# Philippus Elastic4s

# elastic4s - Elasticsearch Scala Client

## Usage

We have created sample projects in both sbt, maven and gradle. Check them out here:
https://github.com/philippus/elastic4s/tree/master/samples

To get started you will need to add a dependency:

- [elastic4s-client-esjava](https://mvnrepository.com/artifact/nl.gn0s1s/elastic4s-client-esjava)

```scala
// major.minor are in sync with the elasticsearch releases
val elastic4sVersion = "x.x.x"
libraryDependencies ++= Seq(
  // recommended client for beginners
  "nl.gn0s1s" %% "elastic4s-client-esjav

```
