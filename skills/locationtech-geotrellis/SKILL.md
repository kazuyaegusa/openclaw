---
name: locationtech-geotrellis
description: "GeoTrellis is a geographic data processing engine for high performance applications."
homepage: https://github.com/locationtech/geotrellis
metadata:
  openclaw:
    emoji: "🗄️"
    auto_generated: true
    requires:
      bins: ["git"]
---

# Locationtech Geotrellis

# GeoTrellis

## Installation

GeoTrellis is currently available for Scala 2.12 and 2.13, using Spark 3.3.x.

To get started with SBT, simply add the following to your build.sbt file:

```scala
libraryDependencies += "org.locationtech.geotrellis" %% "geotrellis-raster" % "<latest version>"
```

To grab the latest `SNAPSHOT`, `RC` or milestone build, add these resolvers:

```scala
// maven central snapshots
resolvers ++= Seq(
  "central-snapshots" at "https://central.sonatype.com/repository/maven-snapshots/"
)

// or eclipse s



```
