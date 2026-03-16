---
name: xerial-sbt-sonatype
description: "A sbt plugin for publishing Scala/Java projects to the Maven central."
homepage: https://github.com/xerial/sbt-sonatype
metadata:
  openclaw:
    emoji: "⚡"
    auto_generated: true
    requires:
      bins: ["git"]
---

# Xerial Sbt Sonatype

# sbt-sonatype plugin

> ⚠️ **Deprecation Notice:** This plugin no longer works as Sonatype has deprecated the legacy API. Please use sbt's native Sonatype support instead. See the [official sbt documentation](https://www.scala-sbt.org/1.x/docs/Using-Sonatype.html) for details.

A sbt plugin for publishing your project to the Maven central repository through the REST API of Sonatype Nexus. Deploying artifacts to Sonatype repository is a requirement for synchronizing your projects to the [Ma

## Usage

To use sbt-sonatype, you need to create a bundle of your project artifacts (e.g., .jar, .javadoc, .asc files, etc.) into a local folder specified by `sonatypeBundleDirectory`. By default, the folder is `(project root)/target/sonatype-staging/(version)`. Add the following `publishTo` setting to create a local bundle of your project:

```scala
publishTo := sonatypePublishToBundle.value
```

With this setting, `publishSigned` will create a bundle of your project to the local staging folder. If the
