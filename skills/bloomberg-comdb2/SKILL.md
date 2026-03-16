---
name: bloomberg-comdb2
description: "Bloomberg's distributed RDBMS"
homepage: https://github.com/bloomberg/comdb2
metadata:
  openclaw:
    emoji: "🔧"
    auto_generated: true
    requires:
      bins: ["cmake", "coreutils", "jq", "node"]
---

# Bloomberg Comdb2

Comdb2 is a clustered RDBMS built on Optimistic Concurrency Control techniques.
It provides multiple isolation levels, including Snapshot and Serializable Isolation.
Read/Write transactions run on any node, with the client library transparently negotiating connections to lowest cost (latency) node which is available.
The client library provides transparent reconnect.

Work on Comdb2 was started at Bloomberg LP in 2004 and it has been under heavy development since.
More information about the ar

## Usage

On every machine in the cluster:

1. Make sure all machines in the cluster can talk to each other via ssh.  
   Copy keys around if needed.

2. Install prerequisites:

   **Debian/Ubuntu**

   ```
   sudo apt-get install -y  \
       bison                \
       build-essential      \
       cmake                \
       flex                 \
       libevent-dev         \
       liblz4-dev           \
       libprotobuf-c-dev    \
       libreadline-dev      \
       libsqlite3-d
   ```
