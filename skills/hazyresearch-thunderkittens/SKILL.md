---
name: hazyresearch-thunderkittens
description: "Tile primitives for speedy kernels"
homepage: https://github.com/HazyResearch/ThunderKittens
metadata:
  openclaw:
    emoji: "🔧"
    auto_generated: true
    requires:
      bins: ["go", "pip", "python3"]
---

# Hazyresearch Thunderkittens

ThunderKittens is built from the hardware up; we do what the silicon tells us. And modern GPUs tell us that they want to work with fairly small tiles of data. A GPU is not really a 1000x1000 matrix multiply machine (even if it is often used as such); it’s a manycore processor where each core can efficiently run ~16x16 matrix multiplies. Consequently, ThunderKittens is built around manipulating tiles of data no smaller than 16x16 values.

ThunderKittens makes a few tricky things easy that enable

## Installation

**ThunderKittens itself is a header-only library**. The library itself does not require any installation; just clone the repo, and include `kittens.cuh`. Easy money.
