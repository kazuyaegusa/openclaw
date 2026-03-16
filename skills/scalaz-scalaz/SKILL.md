---
name: scalaz-scalaz
description: "Principled Functional Programming in Scala"
homepage: https://github.com/scalaz/scalaz
metadata:
  openclaw:
    emoji: "🔧"
    auto_generated: true
---

# Scalaz Scalaz

# Scalaz

## Usage

```scala
import scalaz._
import std.option._, std.list._ // functions and type class instances for Option and List

scala> Apply[Option].apply2(some(1), some(2))((a, b) => a + b)
res0: Option[Int] = Some(3)

scala> Traverse[List].traverse(List(1, 2, 3))(i => some(i))
res1: Option[List[Int]] = Some(List(1, 2, 3))
```

Use of the `Ops` classes, defined under `scalaz.syntax`.

```scala
import scalaz._
import std.list._ // type class instances for List
import syntax.bind._ // syntax for the Bind typ

```
