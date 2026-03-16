---
name: typelevel-cats
description: "Lightweight, modular, and extensible library for functional programming."
homepage: https://github.com/typelevel/cats
metadata:
  openclaw:
    emoji: "🔧"
    auto_generated: true
    requires:
      bins: ["go"]
---

# Typelevel Cats

Cats is a library which provides abstractions for functional programming in the [Scala programming language](https://scala-lang.org).

Scala supports both object-oriented and functional programming, and this is reflected in the hybrid approach of the
standard library. Cats strives to provide functional programming abstractions that are core, [binary compatible](#binary-compatibility-and-versioning), [modular](https://typelevel.org/cats/motivations.html#modularity), [approachable](https://typelev

## Installation

Cats is available for [Scala.js](http://www.scala-js.org/) and [Scala Native](https://www.scala-native.org/), as well as the standard JVM runtime.

Cats relies on improved type inference via the fix for [SI-2712](https://github.com/scala/bug/issues/2712), which is not enabled by default. For **Scala 2.12** you should add the following to your `build.sbt`:

```scala
scalacOptions += "-Ypartial-unification"
```

(Partial unification is on by default since Scala 2.13, the compiler no longer accepts
