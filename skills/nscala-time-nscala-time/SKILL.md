---
name: nscala-time-nscala-time
description: "A new Scala wrapper for Joda Time based on scala-time"
homepage: https://github.com/nscala-time/nscala-time
metadata:
  openclaw:
    emoji: "🔧"
    auto_generated: true
---

# Nscala Time Nscala Time

# nscala-time

[![Maven Central Version](https://img.shields.io/maven-central/v/com.github.nscala-time/nscala-time_3)](https://central.sonatype.com/artifact/com.github.nscala-time/nscala-time_3)
[![scaladoc](https://javadoc.io/badge2/com.github.nscala-time/nscala-time_3/javadoc.svg)](https://javadoc.io/doc/com.github.nscala-time/nscala-time_3)

## Installation

Add the following to your sbt build:

```scala
libraryDependencies += "com.github.nscala-time" %% "nscala-time" % "3.0.0"
```

if you want to use previous versions, [you can find it from here](https://search.maven.org/#search%7Cga%7C1%7Cg%3A%22com.github.nscala-time%22)

## Usage

This is mostly a convenience wrapper around the Joda Time libraries, adding
more pleasant syntax like operators for addition, subtraction, and comparison.
Also, most fields usually available as `getField` are now simply available as
`field`, following the Scala convention. Some instances of `asX` or `toX` have
also been shortened.
