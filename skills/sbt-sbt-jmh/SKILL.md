---
name: sbt-sbt-jmh
description: ""Trust no one, bench everything." - sbt plugin for JMH (Java Microbenchmark Harness)"
homepage: https://github.com/sbt/sbt-jmh
metadata:
  openclaw:
    emoji: "🔧"
    auto_generated: true
    requires:
      bins: ['go']
---

# Sbt Sbt Jmh

# sbt-jmh

SBT plugin for running [OpenJDK JMH](http://openjdk.java.net/projects/code-tools/jmh/) benchmarks.

## JMH about itself:

JMH is a Java harness for building, running, and analysing nano/micro/milli/macro benchmarks written in Java and other languages targeting the JVM.

Please read [nanotrusting nanotime](http://shipilev.net/blog/2014/nanotrusting-nanotime/) and other blog posts on micro-benchmarking (or why most benchmarks are wrong) and make sure your benchmark
