---
name: spotify-scio
description: "A Scala API for Apache Beam and Google Cloud Dataflow."
homepage: https://github.com/spotify/scio
metadata:
  openclaw:
    emoji: "📦"
    auto_generated: true
---

# Spotify Scio

# Scio

## Usage

Download and install the Java Development Kit (JDK) version 11 or higher,
eg. [adoptium](https://adoptium.net/index.html) or [corretto](https://aws.amazon.com/corretto/).

Install [sbt](https://www.scala-sbt.org/1.x/docs/Setup.html).

Use our [giter8 template](https://github.com/spotify/scio.g8) to quickly create a new Scio job repository:

`sbt new spotify/scio.g8`

Switch to the new repo (default `scio-job`) and build it:

```
cd scio-job
sbt stage
```

Run the included word count example:

`t
