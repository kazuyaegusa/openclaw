---
name: atnos-org-eff
description: "Eff monad for cats - https://atnos-org.github.io/eff"
homepage: https://github.com/atnos-org/eff
metadata:
  openclaw:
    emoji: "🧠"
    auto_generated: true
---

# Atnos Org Eff

# eff

## Installation

Eff is published for Scala 3. `eff` core is available for the JVM, ScalaJS and scala-native. Sbt dependency:

```scala
// check maven badge above for latest version
libraryDependencies += "org.atnos" %% "eff" % "8.0.0"

// for Scala 3.3.x
scalacOptions += "-Ykind-projector"

// for latest Scala 3
scalacOptions += "-Xkind-projector"
```

for Scala 2.x

```scala
libraryDependencies += "org.atnos" %% "eff" % "7.0.6"
```
