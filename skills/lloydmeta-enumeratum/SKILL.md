---
name: lloydmeta-enumeratum
description: "A type-safe, reflection-free, powerful enumeration implementation for Scala with exhaustive pattern"
homepage: https://github.com/lloydmeta/enumeratum
metadata:
  openclaw:
    emoji: "🔧"
    auto_generated: true
    requires:
      bins: ["go"]
---

# Lloydmeta Enumeratum

# Enumeratum [![Continuous integration](https://github.com/lloydmeta/enumeratum/actions/workflows/ci.yml/badge.svg)](https://github.com/lloydmeta/enumeratum/actions/workflows/ci.yml) [![codecov](https://codecov.io/gh/lloydmeta/enumeratum/branch/master/graph/badge.svg?token=HNg3LDxnuK)](https://codecov.io/gh/lloydmeta/enumeratum) [![Maven Central](https://img.shields.io/maven-central/v/com.beachape/enumeratum_3)](https://img.shields.io/maven-central/v/com.beachape/enumeratum_3) [![Scala.js](https

## Usage

Using Enumeratum is simple. Just declare your own sealed trait or class `A` that extends `EnumEntry` and implement it as case objects inside
an object that extends from `Enum[A]` as shown below.

```scala

import enumeratum._

sealed trait Greeting extends EnumEntry

object Greeting extends Enum[Greeting] {

  /*
   `findValues` is a protected method that invokes a macro to find all `Greeting` object declarations inside an `Enum`

   You use it to implement the `val values` member
  */
  val val

```
