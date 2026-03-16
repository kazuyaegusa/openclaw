---
name: sbt-sbt-native-packager
description: "sbt Native Packager"
homepage: https://github.com/sbt/sbt-native-packager
metadata:
  openclaw:
    emoji: "⚙️"
    auto_generated: true
    requires:
      bins: ["docker"]
---

# Sbt Sbt Native Packager

# SBT Native Packager

## Installation

Add the following to your `project/plugins.sbt` file:

```scala
// for autoplugins
addSbtPlugin("com.github.sbt" % "sbt-native-packager" % "<version>")
```

In your `build.sbt` enable the plugin you want. For example the
`JavaAppPackaging`.

```scala
enablePlugins(JavaAppPackaging)
```

Or if you need a server with autostart support

```scala
enablePlugins(JavaServerAppPackaging)
```

## Usage

```bash

```
