---
name: google-leveldb
description: "LevelDB is a fast key-value storage library written at Google that provides an ordered mapping from"
homepage: https://github.com/google/leveldb
metadata:
  openclaw:
    emoji: "🔧"
    auto_generated: true
    requires:
      bins: ["git"]
---

# Google Leveldb

LevelDB is a fast key-value storage library written at Google that provides an ordered mapping from string keys to string values.

> **This repository is receiving very limited maintenance. We will only review the following types of changes.**
>
> - Fixes for critical bugs, such as data loss or memory corruption
> - Changes absolutely needed by internally supported leveldb clients. These typically fix breakage introduced by a language/standard library/OS update

[![ci](https://github.com/google/

## Installation

We use a database with a million entries. Each entry has a 16 byte
key, and a 100 byte value. Values used by the benchmark compress to
about half their original size.

    LevelDB:    version 1.1
    Date:       Sun May  1 12:11:26 2011
    CPU:        4 x Intel(R) Core(TM)2 Quad CPU    Q6600  @ 2.40GHz
    CPUCache:   4096 KB
    Keys:       16 bytes each
    Values:     100 bytes each (50 bytes after compression)
    Entries:    1000000
    Raw Size:   110.6 MB (estimated)
    File Size:  62
