---
name: plokhotnyuk-jsoniter-scala
description: "Scala macros for compile-time generation of safe and ultra-fast JSON codecs + circe booster"
homepage: https://github.com/plokhotnyuk/jsoniter-scala
metadata:
  openclaw:
    emoji: "🗄️"
    auto_generated: true
    requires:
      bins: ["curl", "git", "jq", "node"]
---

# Plokhotnyuk Jsoniter Scala

# jsoniter-scala

## Usage

Let's assume that you have the following data structures:

```scala
case class Device(id: Int, model: String)

case class User(name: String, devices: Seq[Device])
```

Add the core library with a "compile" scope and the macros library with "compile-internal" or "provided" scopes to your
list of sbt dependencies:

```sbt
libraryDependencies ++= Seq(
  // Use the %%% operator instead of %% for Scala.js and Scala Native
  "com.github.plokhotnyuk.jsoniter-scala" %% "jsoniter-scala-core" % "2.38.9",


```
