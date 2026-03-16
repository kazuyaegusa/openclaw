---
name: plokhotnyuk-rtree2d
description: "RTree2D is a 2D immutable R-tree for ultra-fast nearest and intersection queries in plane and"
homepage: https://github.com/plokhotnyuk/rtree2d
metadata:
  openclaw:
    emoji: "🗄️"
    auto_generated: true
    requires:
      bins: ["node"]
---

# Plokhotnyuk Rtree2d

# RTree2D

## Usage

Add the library to a dependency list:

```sbt
libraryDependencies += "com.github.plokhotnyuk.rtree2d" %% "rtree2d-core" % "0.11.14"
```

Entries of R-tree are represented by `RTreeEntry` instances which contains payload and 4 coordinates of the minimum
bounding rectangle (MBR) for it.

Add import, create entries, build an R-tree from them, and use it for search a nearest entry or search intersections
by point or rectangle requests:

```scala
import com.github.plokhotnyuk.rtree2d.core._

```
